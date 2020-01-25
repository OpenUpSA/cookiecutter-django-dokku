Cookiecutter for Django in Dokku
================================

Cookiecutter for Django on docker using dokku in prod and docker-compose in dev and test.

Broad principles this project tries to maintain:

- See [12-factor App principles](https://12factor.net/)
- Projects are tested out of the box (including Continuous Integration (CI))
- Prefer stable versions of libraries and services
  - prefer Long Term Support (LTS) versions
  - Don't use the bleeding edge - wait until at least one point-release of a new major version.

Properties of the projects this produces:

- Project directory named by `project_slug`
  - Django project directory named by `project_slug`
  - An initial app directory insite the django project directory named by `app_slug`
- No non-vendor initial models or migrations
- Python dependency management via [Pipenv](https://pypi.org/project/pipenv/)
- Settings relating to security or the correct environment have no default and block startup to ensure they are set explicitly


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
Generate a new Cookiecutter template layout: `cookiecutter gh:OpenUpSA/cookiecutter-django-dokku`


Maintenance
-----------

A fairly convenient dev workflow looks something like:

1. Make a change
2. In a shell in this directory, run `rm -rf /tmp/end_to_end_test/ && time bash -x tests/test_end_to_end.sh`
3. Do what you need to debug
4. In a shell in `/tmp/end_to_end_test`, run `cd . && docker-compose down --volumes`
5. Rinse and repeat.

To modify default dependencies:

1. Run the above to get an environment
2. Get a shell with something like `docker-compose run --rm bash`
3. Make your dependency changes using pipenv
4. Outside the container, copy `Pipenv` and `Pipenv.lock` back to this repository
5. Test your changes using the end-to-end test approach above


License
-------
This project is licensed under the terms of the [MIT License](/LICENSE)
