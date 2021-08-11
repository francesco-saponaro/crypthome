web: daphne -p $PORT -b 0.0.0.0 crypthome.asgi:application
worker: celery -B crypthome worker -events -loglevel info 
