from django.urls import path

from users.views import (
    kakao_redirect,
    login,
    detail
)

app_name = "users"
urlpatterns = [
    path("login/", view=login, name="login"),
    path("kakao_redirect/", view=kakao_redirect, name="kakao_redirect"),
    path("detail/<str:username>/", view=detail, name="detail"),
]
