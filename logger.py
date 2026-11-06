import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = 'logs'
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

file_handler = RotatingFileHandler(
    filename=os.path.join(LOG_DIR, 'app.log'),
    maxBytes=5*1024*1024,
    backupCount=3,
    encoding='utf-8'
)

file_handler.setFormatter(formatter)

root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

if root_logger.hasHandlers():
    root_logger.handlers.clear()


root_logger.addHandler(console_handler)
root_logger.addHandler(file_handler)

logging.getLogger("aiogram.event").setLevel(logging.WARNING)
logging.getLogger("asyncpg").setLevel(logging.WARNING)
logging.getLogger("aiohttp.access").setLevel(logging.WARNING)


def get_logger(name):
    return logging.getLogger(name)

