FROM python:3.7-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

RUN pip install pipenv

COPY . /app
RUN cd /app && pipenv install --system

RUN addgroup --system django \
    && adduser --system --ingroup django django
RUN chown -R django:django /app
USER django

WORKDIR /app