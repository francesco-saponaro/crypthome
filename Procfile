web: daphne -p $PORT -b 0.0.0.0 crypthome.asgi:application
worker: celery worker --app=crypthome.celery.app -l DEBUG
channelsworker: python manage.py runworker -v2