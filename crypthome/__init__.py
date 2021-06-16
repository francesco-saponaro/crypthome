# Import celery app from the celery.py file in current directory
from .celery import app as celery_app

# This will load Celery when Django starts, so that shared_task
# will use this app.
__all__ = ('celery_app',)
