#!/bin/bash
echo "Waiting for postgres..."
#while [[ ! $(nc -z db 5435) ]]; do
#  echo "delaying ..."
#  sleep 0.1
#done
#echo "PostgreSQL started"
export USE_S3=TRUE
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py initadmin
python manage.py seed --mode refresh
python manage.py search_index --create
python manage.py runserver 0.0.0.0:8000
exec "$@"