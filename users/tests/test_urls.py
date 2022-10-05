from django.urls import resolve, reverse

from users.models import User


def test_login():
    assert reverse("users:login") == "/users/login/"
    assert resolve("/users/login/").view_name == "users:login"


def test_detail(user: User):
    assert (
        reverse("users:detail", kwargs={"username": user.username})
        == f"/users/detail/{user.username}/"
    )
    assert resolve(f"/users/detail/{user.username}/").view_name == "users:detail"


def test_redirect():
    assert reverse("users:kakao_redirect") == "/users/kakao_redirect/"
    assert resolve("/users/kakao_redirect/").view_name == "users:kakao_redirect"
