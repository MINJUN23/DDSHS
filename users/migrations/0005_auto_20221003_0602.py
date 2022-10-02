# Generated by Django 3.2.15 on 2022-10-02 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20221003_0210'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicBackground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='RelatedFeild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='blog_link',
        ),
        migrations.AddField(
            model_name='user',
            name='brief_self_introduction',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='contact_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='email_accept',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='homepage_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
