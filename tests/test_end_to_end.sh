# abort on any errors
set -euf -o pipefail

echo Create test app using this template
cookiecutter --no-input -o /tmp . project_slug=name-of-the-project
cd /tmp/name-of-the-project

echo Start wait for postgres to come up
docker-compose up -d db
bin/wait_for_postgres.sh postgres://name-of-the-project@db/name-of-the-project

echo Start the app and wait for it
docker-compose run -d web python manage.py migrate
docker-compose up -d
wget --retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 15 http://localhost:8000
