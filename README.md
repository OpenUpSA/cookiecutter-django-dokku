Cookiecutter for Django in Dokku
================================

Cookiecutter for Django on docker using dokku in prod and docker-compose in dev and test.

Broad principles this project tries to maintain:

- See [OpenUp's development best practises](https://github.com/OpenUpSA/best-practices/blob/master/development.md)
- See [12-factor App principles](https://12factor.net/)
- Projects are tested out of the box (including Continuous Integration (CI))
- Prefer stable versions of libraries and services
  - prefer Long Term Support (LTS) versions
  - Don't use the bleeding edge - wait until at least one point-release of a new major version.

Properties of the projects this produces:

- Same Dockerfile used for dev, test and prod
- Project directory named by `project_slug`
  - Django project directory named by `project_slug`
    - An initial app directory inside the django project directory named by `app_slug`
- No non-vendor initial models or migrations
- Python dependency management via [Pipenv](https://pypi.org/project/pipenv/)
- Settings relating to security or the correct environment have no default and block startup to ensure they are set explicitly
- Passing tests
- Travis-CI
- Codecov.io code coverage reports for CI test runs
- Frontend assets
  - Bundled using [parcel](https://parceljs.org/)
  - Hashed and served using [whitenoise](https://pypi.org/project/whitenoise/) in Django.

Important properties of this cookiecutter:

- Ensure it keeps working
  - End-to-end test that creates and smoke-tests a basic project
- Ensure it's easy to maintain
- Ensure the choices made for projects it creates are explained
- Produce minimal boilerplate by default (lowest common denominator of what we consider well-configured apps) rather than producing everything possible just because it's easy to produce boilerplate using cookiecutter.
  - See [cookiecutter-django](https://github.com/pydanny/cookiecutter-django/) for more of a bleeding edge and experimental showcase of what's possible


Requirements
------------
Install `cookiecutter` command line: `pip install cookiecutter`


Usage
-----

1. Install cookiecutter
2. Run `cookiecutter gh:OpenUpSA/cookiecutter-django-dokku`
3. Answer the questions
4. Initialise a git repository in yout project (`git init`)
5. Profit

To try it out quickly, just create a project im /tmp, accept all the defaults, run `tree` and `docker-compose`:

    $ cookiecutter gh:OpenUpSA/cookiecutter-django-dokku -o /tmp
    full_name [Your name]:
    project_name [My site]: My Django Project
    project_slug [my_django_project]:
    app_slug [polls]: polls
    ...

    $ tree /tmp/my_django_project/
    /tmp/my_django_project/
    ├── docker-compose.yml
    ├── Dockerfile
    ├── manage.py
    ├── my_django_project
    ├── ├── admin.py
    ├── ├── initial_app
    ├── ├── ├── admin.py
    ...

    $ docker-compose up
    WARNING: The DJANGO_DEBUG_TOOLBAR variable is not set. Defaulting to a blank string.
    Creating network "my_django_project_default" with the default driver
    Creating volume "my_django_project_db-data" with default driver
    Building web
    Step 1/9 : FROM python:3.7-slim-buster
     ---> 5b03cb8574a0
    Step 2/9 : ENV PYTHONUNBUFFERED 1
     ---> Using cache
     ---> 67ce14763e07
     ...


Maintenance
-----------

A fairly convenient dev workflow looks something like:

1. Make a change
2. In a shell in this directory, run `rm -rf /tmp/end_to_end_test/ && time bash -x tests/test_end_to_end.sh`
3. Do what you need to debug
4. In a shell in `/tmp/end_to_end_test`, run `cd . && docker-compose down --volumes`
  - You might need to add `--rmi local` to remove and rebuild images
5. Rinse and repeat.

To modify default dependencies:

1. Run the above to get an environment
2. Get a root shell with something like `docker-compose run --rm -u root web bash`
3. Make your dependency changes using pipenv
4. Outside the container, copy `Pipfile` and `Pipfile.lock` back to this repository
5. Test your changes using the end-to-end test approach above


License
-------
This project is licensed under the terms of the [MIT License](/LICENSE)
