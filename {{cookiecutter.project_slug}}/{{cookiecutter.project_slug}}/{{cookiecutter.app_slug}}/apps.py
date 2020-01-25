from django.apps import AppConfig


class {{ cookiecutter.app_classname }}Config(AppConfig):
    name = '{{ cookiecutter.project_slug}}.{{ cookiecutter.app_slug }}'
