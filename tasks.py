import asyncio
from logger import get_logger
from dotenv import load_dotenv
import os
import asyncpg
from datetime import datetime, timedelta, timezone

logger = get_logger(__name__)

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')


def cleanup_history():
    asyncio.run(_async_cleanup())

async def _async_cleanup():
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        one_day_ago = datetime.now(timezone.utc) - timedelta(days=1)
        result = await conn.execute(
            '''DELETE FROM weather_history WHERE created_at < $1''',
            one_day_ago
        )
        logger.info("Очистка БД завершена. %s", result)
        return result
    except Exception:
        logger.exception("Ошибка при очистке БД")
        raise
    finally:
        await conn.close()