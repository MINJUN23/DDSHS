from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ['password', "last_login", "is_superuser", "groups", "profile_photo_link", "active", "email",
                   "is_active", "is_staff", "username", "date_joined", "user_permissions", "academic_backgrounds", "careers", ]
