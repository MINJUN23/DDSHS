from django.urls import path
from django.views.generic import TemplateView

from core.views import api

app_name = "core"
urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    path("api/", api, name="api"),
]
