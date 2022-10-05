from django.contrib.auth import login,logout
from django.forms import modelformset_factory
from django.shortcuts import redirect, render
from django.urls import reverse
from users.models import AcademicBackground, Career, User
from users.forms import UserForm
from mj import mJ
import requests


client_id = "033f113746602cb604db505e4972ed92"


class KakaoLoginException(Exception):
    pass


def get_full_url_from_suffix(request, suffix):
    server_url = request._current_scheme_host
    return server_url + suffix


def get_access_token(request, callback_url):
    code = request.GET.get("code")
    CALLBACK_URL = get_full_url_from_suffix(request, callback_url)
    token_json = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={CALLBACK_URL}&code={code}"
    ).json()
    error = token_json.get("error", None)
    if error:
        raise KakaoLoginException(error)
    else:
        return token_json.get("access_token")


def get_user_info(access_token):
    profile_json = requests.get(
        "https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer {access_token}"},
    ).json()
    kakao_id = str(profile_json.get("id"))
    profile_img_link = profile_json.get("properties").get("profile_image")
    return {"kakao_id": kakao_id, "profile_img_link": profile_img_link}


def login(request):
    redirect_url = get_full_url_from_suffix(
        request, reverse('users:kakao_redirect'))
    return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_url}&response_type=code")


def logout(request):
    logout(request.user)
    return redirect("/")

def kakao_redirect(request):
    try:
        access_token = get_access_token(
            request, reverse("users:kakao_redirect"))
        user_info = get_user_info(access_token)
    except KakaoLoginException:
        return redirect(reverse("users:login"))
    academic_background_formset_factory = modelformset_factory(
                AcademicBackground,
                exclude=["user"], extra=1)
    academic_background_formset = academic_background_formset_factory()
    career_formset_factory = modelformset_factory(
                Career, exclude=["user"],  extra=1)
    career_formset = career_formset_factory()
    if request.method == 'GET':
        if User.objects.filter(username=user_info["kakao_id"]).exists():
            user = User.objects.get(username=user_info["kakao_id"])
            user.profile_photo_link = user_info["profile_img_link"]
            login(request, user)
            return redirect("/")
        else:
            return render(request, "account/signup.html",
                          context={"form": UserForm(),
                                   "career_formset": career_formset,
                                   "academic_background_formset": academic_background_formset,
                                   "kakao_id": user_info["kakao_id"]})
    else:
        username = request.POST.get("username")
        user = UserForm(request.POST, request.FILES).save(commit=False)
        user.username = username
        user.profile_photo_link = user_info["profile_img_link"]
        user.save()
        academic_backrounds = academic_background_formset(request.POST).save(commit=False)
        for academic_background in academic_backrounds:
            academic_background.user = user
            user.save()
        careers = career_formset(request.POST).save(commit=False)
        for career in careers:
            career.user = user
            career.save()
        return redirect("/")


def detail(request):
    pass
