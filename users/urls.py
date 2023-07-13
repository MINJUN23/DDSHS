from django.urls import path

from users.views import detail, kakao_redirect, login, logout

app_name = "users"
urlpatterns = [
    path("login/", view=login, name="login"),
    path("logout/", view=logout, name="logout"),
    path("kakao_redirect/", view=kakao_redirect, name="kakao_redirect"),
    path("detail/<str:username>/", view=detail, name="detail"),
]
