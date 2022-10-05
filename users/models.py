from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


AFFILIATION_CHOICES = (
    ("NATURAL SCIENCE", "자연과학"),
    ("ENGINEERING", "공학 계열"),
    ("MEDICAL", "의학 계열"),
    ("OTHER FIELDS", "기타"),
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
    ("Architectural Engineering", "건축/건설"),
    ("Mechanical Engineering", "기계"),
    ("Industrial Engineering", "산업공학"),
    ("Industrial Design", "산업디자인"),
    ("Biotechnology", "생명공학"),
    ("Medical Engineeing", "의료공학"),
    ("Elctrical & Electronic Engineering", "전기전자"),
    ("Computer Science", "컴퓨터"),
    ("Aerospace Engineering", "항공우주공학"),
    ("Chemical Engineering", "화학"),
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


class AcademicBackground(models.Model):
    starting_year = models.PositiveIntegerField(default=2022)
    ending_year = models.PositiveIntegerField(default=2022, null=True, blank=True)
    degree = models.CharField(max_length=30, choices=(("BS", "이학사"), ("BA", "인문 학사"), ("MS", "이학 석사"),
                              ("MA", "인문학 석사"), ("MBA", "경영학 석사"), ("Ph.D", "박사")), default="BS")
    institution = models.CharField(
        max_length=200, help_text="해외 대학, IST, POSTECH의 경우 영어대문자로 기재바랍니다. 그 외 국내대학교는 **대(ex:서울대)까지만 기재해주세요.")
    major = models.CharField(max_length=200, help_text="한글로 기재바랍니다. 복수전공의 경우 반점(,)으로 표시해주세요.")


class Career(models.Model):
    starting_year = models.PositiveIntegerField(default=2022)
    ending_year = models.PositiveIntegerField(default=2022)
    institution = models.CharField(max_length=200)
    deparment = models.CharField(max_length=200)
    position = models.CharField(max_length=100)


class InterestedField(models.Model):
    field = models.CharField(max_length=200, choices=FIELD_CHOICES)


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
    profile_photo = models.ImageField(upload_to="profile", null=True, blank=True)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    generation = models.PositiveIntegerField(null=True)
    class_of_freshman = models.CharField(max_length=10,
                                         choices=tuple([(f"{i}반", f"{i}반") for i in range(1, 6)])
                                         )
    number_of_freshman = models.CharField(max_length=10,
                                          choices=tuple([(f"{i}번", f"{i}번") for i in range(1, 19)])
                                          )
    contactable_email = models.EmailField(null=True, blank=True)
    contactable_phone_number = models.CharField(max_length=20, null=True, blank=True)

    affiliation = models.CharField(max_length=50, choices=AFFILIATION_CHOICES)
    academic_backgrounds = models.ManyToManyField(AcademicBackground)
    careers = models.ManyToManyField(Career)
    interested_fields = models.ManyToManyField(InterestedField)

    homepage_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    insta_link = models.URLField(null=True, blank=True)
    github_link = models.URLField(null=True, blank=True)
    cv = models.FileField(upload_to="cv", null=True, blank=True)

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
