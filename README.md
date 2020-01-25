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

A fairly convenient dev workflow looks something like

1. Make a change
2. In a shell in this directory, run `rm -rf /tmp/end_to_end_test/ && time bash -x tests/test_end_to_end.sh`
3. Do what you need to debug
4. In a shell in `/tmp/end_to_end_test`, run `cd . && docker-compose down --volumes`
5. Rinse and repeat.

License
-------
This project is licensed under the terms of the [MIT License](/LICENSE)
