from django.apps import AppConfig


class {{ cookiecutter.app_slug.replace('_', '')|titlecase() }}Config(AppConfig):
    name = '{{cookiecutter.app_slug}}'
