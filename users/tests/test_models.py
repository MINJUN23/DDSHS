from users.models import User
from django.test import TestCase
from django.core.exceptions import ValidationError


class UserModelTest(TestCase):

    def test_validate_phone_number(self):
        with self.assertRaises(ValidationError):
            User.validate_phone_number("010-1234-5678")
        User.validate_phone_number("01012345678")
