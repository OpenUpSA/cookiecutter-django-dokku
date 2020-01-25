from django.contrib import admin
from django.urls import include, path

from . import views


urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("initial_app", include("{{cookiecutter.project_slug}}.{{cookiecutter.app_slug}}.urls"),),
    path("admin/", admin.site.urls),
]
