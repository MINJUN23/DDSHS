from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from users.forms import UserAdminChangeForm, UserAdminCreationForm
from users.models import (
    University, AcademicBackground, Career,
    InterestedField, User
    )

User = get_user_model()

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ["acronym", "name"]

@admin.register(AcademicBackground)
class AcademicBackgroundAdmin(admin.ModelAdmin):
    list_display = ["user", "academy_affiliation", "academy_field", "academy_starting_year", "academy_ending_year"]

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ["user", "career_affiliation", "career_field", "career_starting_year", "career_ending_year", "company"]

@admin.register(InterestedField)
class InteretedFieldAdmin(admin.ModelAdmin):
    list_display = ["field"]


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]


