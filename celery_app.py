from celery import Celery
from celery.schedules import crontab
from celery.signals import task_failure, task_postrun, task_prerun

from logger import get_logger

logger = get_logger(__name__)

app = Celery('weather_tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

app.conf.beat_schedule = {
    'cleanup-weather-history-every-night': {
        'task': 'tasks.cleanup_history',
        'schedule': crontab(hour=3, minute=0),
    },
}

app.conf.timezone = 'Asia/Yekaterinburg'
app.conf.enable_utc = False

@task_prerun.connect
def task_started(task_id, task, *args, **kwargs):
    logger.info("▶️ Старт таска %s (ID: %s)", task.name, task_id)

@task_postrun.connect
def task_finished(task_id, task, retval, *args, **kwargs):
    logger.info("✅ Таск %s завершён (ID: %s)", task.name, task_id)

@task_failure.connect
def task_failed(task_id, exception, traceback, *args, **kwargs):
    sender = kwargs.get('sender')
    task_name = sender.name if sender else 'Unknown'
    logger.error("❌ Таск %s упал с ошибкой: %s", task_name, exception)