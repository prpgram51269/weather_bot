import asyncpg

class Database():
    def __init__(self, url):
        self.url = url
        self.pool = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(self.url)

    async def add_users(self, user_id, city):
        async with self.pool.acquire() as conn:
            await conn.execute(
                '''INSERT INTO users (user_id, city) VALUES($1, $2) ON CONFLICT (user_id) DO UPDATE SET city = EXCLUDED.city''',
                user_id, city
            )

    async def get_user_city(self, user_id):
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow(
                '''SELECT city FROM users WHERE user_id=$1''',
                user_id
            )
            if row and row['city']:
                return row['city']
            return None

    async def add_weather_history(self, user_id, city):
        async with self.pool as conn:
            await conn.execute(
                '''INSERT INTO weather_history (user_id, city) VALUES ($1, $2)''',
                user_id, city
            )