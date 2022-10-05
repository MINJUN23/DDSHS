from django.urls import reverse
from django.test import TestCase, Client


class UserViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        # self.user = User.objects.get(email="gunpollo1886@gmail.com")
        # self.logined_client = Client().force_login(self.user)

    def test_login(self):
        response = self.client.get(reverse("users:login"))
        assert response.url.find("https://kauth.kakao.com/oauth/authorize") != -1
