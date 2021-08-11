web: gunicorn crypthome.wsgi:application
celeryworker: celery worker --app=crypthome.taskapp --loglevel=info
channelsworker: python manage.py runworker -v2