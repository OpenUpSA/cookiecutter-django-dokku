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

RUN addgroup --system django \
    && adduser --system --ingroup django django

RUN pip install pipenv

# Requirements are installed here to ensure they will be cached.
COPY ./Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt && \
    pip install -r /tmp/requirements.txt

USER django

WORKDIR /app