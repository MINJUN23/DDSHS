# Generated by Django 4.1.2 on 2022-10-06 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0013_rename_deparment_career_department"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="number_of_freshman",
            field=models.CharField(
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
    ]