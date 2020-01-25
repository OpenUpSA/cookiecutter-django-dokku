from django.views import generic


class Home(generic.TemplateView):
    template_name = "{{cookiecutter.app_slug}}/home.html"
