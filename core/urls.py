from django.urls import path

from core.views import about, api, home

app_name = "core"
urlpatterns = [
    path("",home, name="home"),
    path(
        "about/", about, name="about"
    ),
    path("api/", api, name="api"),
]
