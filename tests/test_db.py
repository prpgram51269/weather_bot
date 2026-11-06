import os

def test_env_is_set():
    # Проверяем, что переменная окружения существует
    assert os.getenv("DATABASE_URL") is not None