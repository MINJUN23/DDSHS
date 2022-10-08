from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import serializers

from users.models import AcademicBackground, Career, InterestedField, User


class AcademicBackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicBackground
        fields = ['academy_affiliation', 'academy_field', 'academy_starting_year',
        "academy_ending_year", "degree", "institution", "major"]

class CareerFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ['career_starting_year', 'career_ending_year', 'career_affiliation',
        "career_field","company","department","position"]

class InterestedFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestedField
        fields = ['field']

class UserSerializer(serializers.ModelSerializer):
    academic_backgrounds = AcademicBackgroundSerializer(many=True, read_only=True)
    careers = CareerFieldSerializer(many=True, read_only=True)
    interested_fields = InterestedFieldSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ["name","profile_photo_link", "generation","class_of_freshman",
        "number_of_freshman", "contactable_email", "contactable_phone_number",
        "homepage_link", "linkedin_link", "insta_link", "github_link", "cv_link",
        "contact_description", "brief_self_introduction", "academic_backgrounds",
        "careers", "interested_fields", "cv"
        ]

# Create your views here.

def filter_by_search_text(users, search_text):
    career_Q = Q(position__contains=search_text)|Q(department__contains=search_text)\
            |Q(company__contains=search_text)
    careers = Career.objects.filter(career_Q)     
    academic_backgrounds=AcademicBackground.objects.filter(major__contains=search_text)
    search_Q = Q(name__contains=search_text)|Q(contactable_email__contains=search_text)\
            |Q(contactable_phone_number__contains=search_text)|Q(homepage_link__contains=search_text)\
            |Q(linkedin_link__contains=search_text)|Q(insta_link__contains=search_text)\
            |Q(github_link__contains=search_text)|Q(contact_description__contains=search_text)\
            |Q(brief_self_introduction__contains=search_text)|Q(careers__in=careers)\
            |Q(academic_backgrounds__in=academic_backgrounds)
    return users.filter(search_Q)

def filter_by_institution(users, institution):
    academic_backgrounds=AcademicBackground.objects.filter(institution=institution)
    return users.filter(academic_backgrounds__in=academic_backgrounds)


def filter_by_affiliation(users, affiliation):
    academic_backgrounds=AcademicBackground.objects.filter(academy_affiliation=affiliation)
    careers=Career.objects.filter(career_affiliation=affiliation)
    affilation_Q = Q(academic_backgrounds__in=academic_backgrounds)|Q(careers__in=careers)
    return users.filter(affilation_Q)

def filter_by_major_field(users, major_field):
    academic_backgrounds=AcademicBackground.objects.filter(academy_field=major_field)
    careers=Career.objects.filter(career_field=major_field)
    major_field_Q = Q(academic_backgrounds__in=academic_backgrounds)|Q(careers__in=careers)
    return users.filter(major_field_Q)

def filter_by_intested_field(users, interested_field):
    interested_fields=InterestedField.objects.filter(field=interested_field)
    return users.filter(interested_fields__in=interested_fields)

def filter_by_generation(users, generation):
    return users.filter(generation=generation)

def api(request):
    search_text = request.GET.get('search_text',None)
    institution = request.GET.get('instiution',None)
    affiliation = request.GET.get('affiliation',None)
    major_field = request.GET.get('major_field',None)
    interested_field=request.GET.get('interested_field',None)
    generation = request.GET.get('generation',None)

    users = User.objects.filter(is_superuser=False)
    if search_text:
        users = filter_by_search_text(users, search_text)
    if institution:
        users = filter_by_institution(users, institution)
    if affiliation:
        users = filter_by_affiliation(users,affiliation)
    if major_field:
        users = filter_by_major_field(users, major_field)
    if interested_field:
        users = filter_by_intested_field(users, interested_field)
    if generation:
        users = filter_by_generation(users, generation)
    users_context = [UserSerializer(user).data for user in users]
    return JsonResponse({"users":users_context})


def home(request):
    if request.user.is_authenticated:
        return render(request,"pages/home.html", context={"users":User.objects.all()})
    else:
        return render(request,"pages/need_login.html")

def about(request):
    if request.user.is_authenticated:
        return render(request,"pages/about.html")
    else:
        return render(request,"pages/need_login.html")
