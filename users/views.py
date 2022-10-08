import requests
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.forms import modelformset_factory
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import UserForm
from users.models import AcademicBackground, Career, User

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
    if request.user.is_authenticated:
        return redirect("/")
    redirect_url = get_full_url_from_suffix(
        request, reverse('users:kakao_redirect'))
    return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_url}&response_type=code")


def logout(request):
    logout_user(request)
    return redirect("/")

def kakao_redirect(request):
    academic_background_formset_factory = modelformset_factory(
                AcademicBackground,exclude=["user"],
                    extra=1,can_delete = True)
    academic_background_formset = academic_background_formset_factory(prefix="academic_background_form")
    career_formset_factory = modelformset_factory(Career,exclude=["user"],
                   extra=1,can_delete = True)
    career_formset = career_formset_factory(prefix="career_form")
    if request.method == 'GET':
        try:
            access_token = get_access_token(
                request, reverse("users:kakao_redirect"))
            user_info = get_user_info(access_token)
        except KakaoLoginException:
            return redirect(reverse("users:login"))
        if User.objects.filter(username=user_info["kakao_id"]).exists():
            user = User.objects.get(username=user_info["kakao_id"])
            user.profile_photo_link = user_info["profile_img_link"]
            login_user(request, user)
            return redirect("/")
        else:
            return render(request, "account/signup.html",
                          context={"form": UserForm(),
                                   "career_formset": career_formset,
                                   "academic_background_formset": academic_background_formset,
                                    "kakao_id": user_info["kakao_id"],
                                    "proflie_img_link": user_info["profile_img_link"],
                                   })
    else:
        username = request.POST.get("username")
        try:
            user = UserForm(request.POST, request.FILES).save(commit=False)
            user.username = username
            user.profile_photo_link = request.POST.get("username")
            user.save()
            academic_background_formset = academic_background_formset_factory(
                        request.POST,
                        queryset=AcademicBackground.objects.none(),
                        prefix="academic_background_form")
            if academic_background_formset.is_valid():
                academic_backgrounds = academic_background_formset.save(commit=False)
                for academic_background in academic_backgrounds:
                    academic_background.user = user
                    academic_background.save()
            else:
                for error in academic_background_formset.errors:
                    print(error)
            career_formset = career_formset_factory(
                    request.POST,
                    queryset=Career.objects.none(),
                    prefix="career_form")
            if career_formset.is_valid():
                careers = career_formset.save(commit=False)
                for career in careers:
                    career.user = user
                    career.save()
            else:
                for error in academic_background_formset.errors:
                    print(error)
            login_user(request,user)
            return redirect("/")
        except Exception as e:
            print(e)
            User.objects.get(username=username).delete()
            return redirect(reverse("users:login"))


def detail(request,username):
    user = User.objects.get(username=username)
    academic_background_formset_factory = modelformset_factory(
                AcademicBackground,exclude=["user"],
                    extra=1,can_delete = True)
    academic_background_formset = academic_background_formset_factory(queryset=user.academic_backgrounds.all())
    career_formset_factory = modelformset_factory(Career,exclude=["user"],
                   extra=1,can_delete = True)
    career_formset = career_formset_factory(queryset=user.careers.all())
    return render(request, "account/detail.html", context={"form": UserForm(instance=user),
                                   "career_formset": career_formset,
                                   "academic_background_formset": academic_background_formset,
                                   })
