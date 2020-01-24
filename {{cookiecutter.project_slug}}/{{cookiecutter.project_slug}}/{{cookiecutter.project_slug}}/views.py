from django.views import generic


class Home(generic.TemplateView):
    template_name = "{{cookiecutter.project_slug}}/home.html"
