web: gunicorn stockman_project.wsgi —-log-file -
worker: celery worker --app=stockman_project
beat: celery beat --loglevel=info -app=stockman_project