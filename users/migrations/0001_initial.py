# Generated by Django 4.1.2 on 2023-07-13 07:35

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="InterestedField",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "field",
                    models.CharField(
                        choices=[
                            ("Architectural Engineering", "건축/건설 공학"),
                            ("Business", "경영학"),
                            ("Economics", "경제학"),
                            ("Pedagogy", "교육학"),
                            ("Mechanical Engineering", "기계공학"),
                            ("Physics", "물리학"),
                            ("Law", "법학"),
                            ("Industrial Engineering", "산업공학"),
                            ("Industrial Design", "산업디자인"),
                            ("Biotechnology", "생명공학"),
                            ("Biology", "생명과학"),
                            ("Veterinary Medicine", "수의학"),
                            ("Mathematics", "수학"),
                            ("Pharmacy", "약학"),
                            ("Medical Engineeing", "의료공학"),
                            ("Medicine", "의학"),
                            ("Elctrical & Electronic Engineering", "전기전자"),
                            ("Earth Science", "지구과학"),
                            ("Astronomy", "천문학"),
                            ("Dental Medicine", "치의학"),
                            ("Computer Science", "컴퓨터공학"),
                            ("Korean Medicine", "한의학"),
                            ("Aerospace Engineering", "항공우주공학"),
                            ("Chemistry", "화학"),
                            ("Chemical Engineering", "화학공학"),
                            ("Environmental Engineering", "환경공학"),
                        ],
                        max_length=200,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("updated", models.DateTimeField(auto_now=True, null=True)),
                ("profile_photo_link", models.URLField(max_length=1000)),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Name of User"
                    ),
                ),
                (
                    "generation",
                    models.CharField(
                        choices=[
                            ("1", "1기"),
                            ("2", "2기"),
                            ("3", "3기"),
                            ("4", "4기"),
                            ("5", "5기"),
                            ("6", "6기"),
                            ("7", "7기"),
                            ("8", "8기"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "class_of_freshman",
                    models.CharField(
                        choices=[
                            ("1반", "1반"),
                            ("2반", "2반"),
                            ("3반", "3반"),
                            ("4반", "4반"),
                            ("5반", "5반"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "number_of_freshman",
                    models.CharField(
                        choices=[
                            ("1번", "1번"),
                            ("2번", "2번"),
                            ("3번", "3번"),
                            ("4번", "4번"),
                            ("5번", "5번"),
                            ("6번", "6번"),
                            ("7번", "7번"),
                            ("8번", "8번"),
                            ("9번", "9번"),
                            ("10번", "10번"),
                            ("11번", "11번"),
                            ("12번", "12번"),
                            ("13번", "13번"),
                            ("14번", "14번"),
                            ("15번", "15번"),
                            ("16번", "16번"),
                            ("17번", "17번"),
                            ("18번", "18번"),
                            ("19번", "19번"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "contactable_email",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                (
                    "contactable_phone_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "homepage_link",
                    models.URLField(blank=True, max_length=1000, null=True),
                ),
                (
                    "linkedin_link",
                    models.URLField(blank=True, max_length=1000, null=True),
                ),
                ("insta_link", models.URLField(blank=True, max_length=1000, null=True)),
                (
                    "github_link",
                    models.URLField(blank=True, max_length=1000, null=True),
                ),
                ("cv", models.FileField(blank=True, null=True, upload_to="cv")),
                ("cv_link", models.URLField(blank=True, max_length=1000, null=True)),
                ("email_accept", models.BooleanField(default=False)),
                ("contact_description", models.TextField(blank=True, null=True)),
                ("brief_self_introduction", models.TextField(blank=True, null=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "interested_fields",
                    models.ManyToManyField(to="users.interestedfield"),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
