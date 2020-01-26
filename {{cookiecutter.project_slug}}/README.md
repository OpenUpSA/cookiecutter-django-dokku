{{ cookiecutter.project_name }}
===============================


Complete project setup
----------------------

- [ ] Initialise a git repository in this directory
  - [ ] Explicitly add directories needed for collectstatic to work: `git add -f staticfiles/.gitkeep end_to_end_test/static/.gitkeep`
- [ ] Create a repository on [GitHub](https://github.com/OpenUpSA) and add as a remote to this repository
  - e.g. `git remote add origin git@github.com:OpenUpSA/{{ cookiecutter.project_slug }}.git`
- [ ] Enable Continuous Integration checks for the GitHub Repository at [travis-ci.org](https://travis-ci.org)
- [ ] Enable code coverage reporting for the project at [codecov.io](https://codecov.io)
  - [ ] Enable GitHub integration - it automatically configures Travis-CI and shows coverage diffs in pull requests
  - [ ] Verify that you see coverage % on the Commits tab for the project. If it's just zero, check for errors by clicking a commit item.


Project Layout
--------------

### Docker

This directory is mapped as a volume in the app. This can result in file permission errors like `EACCES: permission denied`. File permissions are generally based on UID integers and not usernames, so it doesn't matter what users are called, UIDs have to match or be mapped to the same numbers between the host and container.

We want to avoid running as root in production (even inside a container) and we want production to be as similar as possible to dev and test.

The easiest solution is to make this directory world-writable so that the container user can write to install/update stuff. Be aware of the security implications of this. e.g. `chmod -R 777 .`

Another good option is to specify the user ID to run as in the container. A persistent way to do that is by specifying `user: ${UID}:${GID}` in a `docker-compose.yml` file, perhaps used as an overlay, and specifying your host user's IDs in an environment file used by docker-compose, e.g. `.env`.


### Django

Apps go in the project directory `{{ cookiecutter.project_slug }}`

### Python

Dependencies are managed via Pipfile, e.g.

    pipenv install whitenoise[brotli]==1.2.3
    docker-compose run --rm web pipenv install --system

Make sure to commit updates to Pipfile and Pipfile.lock to git


### Javascript and CSS

JS and CSS are bundled using [parcel](https://parceljs.org/) - see `package.json`.

Dependencies are managed via `yarn`, e.g.

    docker-compose run --rm web yarn add bootstrap@4.x

Make sure to commit updates to package.json and yarn.lock to git.


Development setup
-----------------

In one shell, run the frontend asset builder

    docker-compose run --rm yarn dev


In another shell, initialise and run the django app

    docker-compose run --rm web bin/wait-for-postgres.sh
    docker-compose run --rm web python manage.py migrate
    docker-compose run --rm web up


If you need to destroy and recreate your dev setup, e.g. if you've messed up your
database data or want to switch to a branch with an incompatible database schema,
you can destroy all volumes and recreate them by running the following, and running
the above again:

    docker-compose down --volumes


Running tests
-------------

    docker-compose run --rm web python manage.py test

Tests might fail to connect to the databse if the docker-compose `db` service wasn't running and configured yet. Just check the logs for the `db` service and run the tests again.
