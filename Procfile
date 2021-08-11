web: daphne -p $PORT -b 0.0.0.0 crypthome.asgi:application
worker: celery -A crypthome worker -l info
channelsworker: python manage.py runworker -v2