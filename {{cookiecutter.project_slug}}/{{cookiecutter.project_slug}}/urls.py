from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("{{cookiecutter.app_slug}}.urls")),

    path('admin/', admin.site.urls),
]
