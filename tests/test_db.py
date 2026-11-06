from pytest_asyncio import fixture

from database import Database

TEST_DB_URL = "postgresql://postgres:secret@localhost:5432/weather_bot"

@fixture
async def db():
    database = Database(TEST_DB_URL)
    await database.connect()
    yield database

    async with database.pool.acquire() as conn:
        await conn.execute('''DELETE FROM users WHERE user_id=99999''')
    await database.pool.close()


async def test_add_and_get_user(db):
    user_id = 99999
    city = 'Moscow'
    await db.add_users(user_id, city)

    result = await db.get_user_city(user_id)
    assert result == city

    await db.add_users(user_id, 'Paris')
    update_inf = await db.get_user_city(user_id)
    assert update_inf == 'Paris'