Running tests
-------------

    docker-compose run --rm web python manage.py test

Tests might fail to connect tot he databse if the docker-compose `db` service wasn't running and configured yet. Just check the logs for the `db` service and run the tests again.

## Coverage

Ensure the host directory where docker-compose is run from is writable by the UID inside the container. The easiest way to do that is to make it globally-writable, e.g. `chmod 777 .` but be aware of the security implications of this.

Adding dependencies using Pipenv
--------------------------------

Run the container as root to have permission to change files

    docker-compose run -u root web bash

and in that shell install what you need
