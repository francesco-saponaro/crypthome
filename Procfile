web: daphne therapist_portal.asgi:application --port $PORT --bind 0.0.0.0
celeryworker: celery worker --app=crypthome.taskapp --loglevel=info
channelsworker: python manage.py runworker -v2