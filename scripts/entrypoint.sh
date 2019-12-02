#!/bin/bash
echo "Waiting for postgres..."
#while [[ ! $(nc -z db 5435) ]]; do
#  echo "delaying ..."
#  sleep 0.1
#done
#echo "PostgreSQL started"
python manage.py migrate
python manage.py initadmin
python manage.py seed --mode refresh
python manage.py runserver 0.0.0.0:8000
exec "$@"