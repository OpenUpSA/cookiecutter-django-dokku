# abort on any errors
set -euf -o pipefail

PROJECT_NAME=end_to_end_test
PROJECT_DIR=/tmp/${PROJECT_NAME}

#!/bin/bash
function finish {
    cd ${PROJECT_DIR}
    docker-compose logs db
    docker-compose logs web
}
trap finish EXIT


echo Create test app using this template
cookiecutter --no-input -o /tmp . project_name="End to end test" app_slug=initial_app
cd ${PROJECT_DIR}

echo Start wait for postgres to come up
docker-compose up -d db
bin/wait_for_postgres.sh postgres://${PROJECT_NAME}@db/${PROJECT_NAME}

echo Start the app and wait for it
docker-compose run -d web python manage.py migrate
docker-compose up -d
wget --retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 5 -O - http://localhost:8000 | \
     grep "This is the homepage for"
wget --retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 5 -O - http://localhost:8000/initial_app | \
     grep "This is the index for"
