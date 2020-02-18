#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset


python manage.py collectstatic --noinput
gunicorn  --worker-class gevent zanews.wsgi:application --log-file - --bind 0.0.0.0:5000
