Cookiecutter for Django in Dokku
================================

Cookiecutter for Django on docker using dokku in prod and docker-compose in dev and test.

Requirements
------------
Install `cookiecutter` command line: `pip install cookiecutter`

Usage
-----
Generate a new Cookiecutter template layout: `cookiecutter gh:OpenUpSA/cookiecutter-django-dokku`

Maintenance
-----------

The best way I've found to maintain this so far is to hand-code the Dockerfile and docker-compose.yml to a point that I can get a container running, then update things like Pipenv.* and django boilerplate from a root shell in the container. The files are mapped out to the host using docker-compose so I can copy them back into the cookiecutter template, checking git diffs to make sure only the desired changes are made and nothing is overwritten unintentionally. Something like:

This should be taken as pseudocode - there are almost certainly path mistakes here.

On dev host

    cookiecutter . -o /tmp/myproject
    cd /tmp/myproject
    docker-compose run -u root web bash

Inside web shell started above

    cd /app
    pipenv install X==y.2.3
    django-admin startproject DEADBEEF .
    django-admin startapp DEADBEEF

On dev host in cookiecutter template dir

   cp /tmp/myproject/DEADBEEF \{\{cookiecutter.project_slug\}\}/
   mv \{\{cookiecutter.project_slug\}\}/DEADBEEF \{\{cookiecutter.project_slug\}\}/\{\{cookiecutter.project_slug\}\}/
   find . -type f -name "*.py" -print0 | xargs -0 sed -i'' -e 's/DEADBEEF/{{cookiecutter.project_slug}}/g'
   git diff
   git add ...
   git commit -m ...

Then start back at the top and verify that it does what's intended.

License
-------
This project is licensed under the terms of the [MIT License](/LICENSE)
