web: gunicorn stockman_project.wsgi —-log-file -
worker: celery worker --loglevel=info -A stockman_project
beat: celery beat --loglevel=info -A stockman_project