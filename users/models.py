from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError

from datetime import datetime

AFFILIATION_CHOICES = (
    ("NATURAL SCIENCE", "자연과학 계열"),
    ("ENGINEERING", "공학 계열"),
    ("MEDICAL", "의학 계열"),
    ("OTHER FIELDS", "기타 계열"),
)

NATURAL_SCIENCE_CHOICES = (
    ("Physics", "물리학"),
    ("Biology", "생명과학"),
    ("Mathematics", "수학"),
    ("Earth Science", "지구과학"),
    ("Astronomy", "천문학"),
    ("Chemistry", "화학"),
)


MEDICAL_FIELD_CHOICES = (
    ("Veterinary Medicine", "수의학"),
    ("Medicine", "의학"),
    ("Pharmacy", "약학"),
    ("Dental Medicine", "치의학"),
    ("Korean Medicine", "한의학"),
)

ENGINEERING_CHOICES = (
    ("Architectural Engineering", "건축/건설 공학"),
    ("Mechanical Engineering", "기계공학"),
    ("Industrial Engineering", "산업공학"),
    ("Industrial Design", "산업디자인"),
    ("Biotechnology", "생명공학"),
    ("Medical Engineeing", "의료공학"),
    ("Elctrical & Electronic Engineering", "전기전자"),
    ("Computer Science", "컴퓨터공학"),
    ("Aerospace Engineering", "항공우주공학"),
    ("Chemical Engineering", "화학공학"),
    ("Environmental Engineering", "환경공학"),
    ("ETC", "기타"),
)


OTHER_FIELD_CHOCICES = (
    ("Business", "경영학"),
    ("Economics", "경제학"),
    ("Pedagogy", "교육학"),
    ("Law", "법학"),
    ("ETC", "기타"),
)

FIELD_CHOICES = (list(NATURAL_SCIENCE_CHOICES)+list(MEDICAL_FIELD_CHOICES) +
                 list(ENGINEERING_CHOICES[:-1])+list(OTHER_FIELD_CHOCICES[:-1]))
FIELD_CHOICES.sort(key=lambda x: x[1])

GENERATION_CHOICES = tuple([(str(year), f"{year}기")for year in range(1, datetime.now().year-2014)])

YEAR_CHOICES = tuple([(str(year), str(year))for year in range(2014, datetime.now().year+1)])


class University(models.Model):
    class Meta:
        ordering = ["name", 'acronym']

    name = models.CharField(max_length=200)
    acronym = models.CharField(max_length=20)

    @classmethod
    def get_university_list(cls):
        # return (("", ''),)
        return tuple([(university.name, f"{university.name}({university.acronym})") for university in University.objects.all()])

    def __str__(self):
        return f"{self.name} - {self.acronym}"


class AcademicBackground(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="academic_backgrounds", null=True)
    academy_affiliation = models.CharField(max_length=50, choices=AFFILIATION_CHOICES)
    academy_field = models.CharField(max_length=50, choices=FIELD_CHOICES)
    academy_starting_year = models.CharField(max_length=10, default="2022", choices=YEAR_CHOICES)
    academy_ending_year = models.CharField(max_length=10, choices=YEAR_CHOICES, null=True, blank=True)
    degree = models.CharField(max_length=30, choices=(("BS", "이학사"), ("BA", "인문 학사"), ("MS", "이학 석사"),
                              ("MA", "인문학 석사"), ("MBA", "경영학 석사"), ("Ph.D", "박사")), default="BS")
    institution = models.CharField(max_length=200, choices=University.get_university_list())
    major = models.CharField(max_length=200, help_text="한글로 기재바랍니다. 복수전공의 경우 반점(,)으로 표시해주세요.")


class Career(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='careers', null=True)
    career_affiliation = models.CharField(max_length=50, choices=AFFILIATION_CHOICES)
    career_field = models.CharField(max_length=50, choices=FIELD_CHOICES)
    career_starting_year = models.CharField(max_length=10, default="2022", choices=YEAR_CHOICES)
    career_ending_year = models.CharField(max_length=10, choices=YEAR_CHOICES, null=True, blank=True)
    company = models.CharField(max_length=200)
    deparment = models.CharField(max_length=200)
    position = models.CharField(max_length=100)


class InterestedField(models.Model):
    field = models.CharField(max_length=200, choices=FIELD_CHOICES)

    def __str__(self):
        return f"{self.get_field_display()}"


class User(AbstractUser):
    """
    Default custom user model for DDSHS.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    updated = models.DateTimeField(auto_now=True, null=True)

    first_name = None  # type: ignore
    last_name = None  # type: ignore
    profile_photo_link = models.URLField()
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    generation = models.CharField(max_length=10, choices=GENERATION_CHOICES)
    class_of_freshman = models.CharField(max_length=10,
                                         choices=tuple([(f"{i}반", f"{i}반") for i in range(1, 6)])
                                         )
    number_of_freshman = models.CharField(max_length=10,
                                          choices=tuple([(f"{i}번", f"{i}번") for i in range(1, 19)])
                                          )
    contactable_email = models.EmailField(null=True, blank=True)
    contactable_phone_number = models.CharField(max_length=20, null=True, blank=True)

    interested_fields = models.ManyToManyField(InterestedField)

    homepage_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    insta_link = models.URLField(null=True, blank=True)
    github_link = models.URLField(null=True, blank=True)
    cv = models.FileField(upload_to="cv", null=True, blank=True)
    cv_link = models.URLField(null=True, blank=True)

    email_accept = models.BooleanField(default=False)

    contact_description = models.TextField(blank=True, null=True)
    brief_self_introduction = models.TextField(blank=True, null=True)

    def validate_phone_number(phone_number):
        for char in phone_number:
            try:
                int(char)
            except:
                raise ValidationError(_('%(value)s is not an even number'),
                                      params={'phone_number': phone_number},)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
