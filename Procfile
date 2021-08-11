web: daphne crypthome.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: celery worker --app=tasks.app
