from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# MEDICAL_FIELD_CHOICES = (
#     ("Medicine", "의학"),
#     ("Pharmacy", "약학"),
#     ("Veterinary Medicine", "수의학"),
# )

# ENGINERRING_CHOICES = (
#     ("Engineering", "공학 일반"),
#     ("Architectural Engineering", "건축공학"),
#     ("Mechanical Engineering", "기계공학"),
#     ("Urban Planning", "도시공학"),
#     ("Robotics", "로봇공학"),
#     ("Industrial Engineering", "산업공학"),
#     ("Industrial Design", "산업디자인"),
#     ("Biotechnology", "생명공학"),
#     ("Food Engineering", "식품공학"),
#     ("Energy Engineering", "에너지공학"),
#     ("Artistic Engineering", "예술공학"),
#     ("Medical Engineeing", "의료공학"),
#     ("Materials Engineering", "재료공학"),
#     ("Electrical Engineering", "전기공학"),
#     ("Electronic Engineering", "전자공학"),
#     ("Computer Science", "컴퓨터공학"),
#     ("Aerospace Engineering", "항공우주공학"),
#     ("Chemical Engineering", "화학공학"),
#     ("Environmental Engineering", "환경공학"),
# )

# NATURAL_SCIENCE_CHOICES = [
#     ("Physics", "물리학"),
#     ("Biology", "생명과학"),
#     ("Mathematics", "수학"),
#     ("Earth Science", "지구과학"),
#     ("Astronomy", "천문학"),
#     ("Chemistry", "화학"),
# ]


class User(AbstractUser):
    """
    Default custom user model for DDSHS.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    first_name = None  # type: ignore
    last_name = None  # type: ignore

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

    homepage_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    insta_link = models.URLField(null=True, blank=True)
    github_link = models.URLField(null=True, blank=True)

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


class AcademicBackground(models.Model):
    pass


class RelatedFeild(models.Model):
    pass
