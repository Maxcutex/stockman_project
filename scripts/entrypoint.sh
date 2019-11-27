#!/bin/bash
echo "Waiting for postgres..."
#while [[ ! $(nc -z db 5435) ]]; do
#  echo "delaying ..."
#  sleep 0.1
#done
#echo "PostgreSQL started"
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@stockman.com', 'pass')" | ./manage.py shell
python manage.py runserver 0.0.0.0:8000
exec "$@"