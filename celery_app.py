from celery import Celery
from celery.schedules import crontab

app = Celery('weather_tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

app.conf.beat_schedule = {
    'cleanup-weather-history-every-night': {
        'task': 'tasks.cleanup_history',
        'schedule': crontab(hour=3, minute=0),
    },
}

app.conf.timezone = 'Asia/Yekaterinburg'
app.conf.enable_utc = False