FROM openup/docker-python-nodejs:python3.7-nodejs12

ENV PYTHONUNBUFFERED 1
ENV NODE_ENV production

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # git for codecov file listing
  && apt-get install -y git \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

RUN pip install pipenv

# Copy, then install requirements before copying rest for a requirements cache layer.
COPY Pipfile* /tmp/
RUN cd /tmp \
    && pipenv install --system

COPY . /app

RUN addgroup --system django \
    && adduser --system --ingroup django django
RUN chown -R django:django /app
USER django

WORKDIR /app

RUN yarn && yarn build

EXPOSE 5000
CMD /app/bin/start.sh