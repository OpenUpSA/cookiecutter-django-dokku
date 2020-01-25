Running tests
-------------

    docker-compose run --rm web python manage.py test

Tests might fail to connect tot he databse if the docker-compose `db` service wasn't running and configured yet. Just check the logs for the `db` service and run the tests again.


Adding dependencies using Pipenv
--------------------------------

Run the container as root to have permission to change files

    docker-compose run -u root web bash

and in that shell install what you need
