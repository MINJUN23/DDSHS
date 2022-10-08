from django.test import TestCase

from users.management.commands.create_test_users import (
    create_test_user,
    set_academic_backgrounds,
    set_careers,
)
from users.management.commands.set_default_universities import set_universities
from users.management.commands.set_interested_fields import set_interested_fields
from users.models import AcademicBackground, Career


class UserCommandTest(TestCase):
    def setUp(self):
        set_universities()
        set_interested_fields()
        self.user = create_test_user(0)
    
    def test_set_careers(self):
        before_count = Career.objects.all().count()
        set_careers(self.user)
        after_count = Career.objects.all().count()
        assert after_count>before_count

    def test_set_academic_backgrounds(self):
        before_count = AcademicBackground.objects.all().count()
        set_academic_backgrounds(self.user)
        after_count = AcademicBackground.objects.all().count()
        assert after_count>before_count

    def test_create_test_user(self):
        create_test_user(1)


