docker-compose run --rm db psql --set ON_ERROR_STOP=1 $1 -c "select 'hello';"
