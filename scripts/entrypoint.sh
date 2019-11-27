#!/bin/bash
echo "Waiting for postgres..."
#while [[ ! $(nc -z db 5435) ]]; do
#  echo "delaying ..."
#  sleep 0.1
#done
#echo "PostgreSQL started"
exec "python manage.py migrate"
exec "python manage.py runserver"
exec "$@"