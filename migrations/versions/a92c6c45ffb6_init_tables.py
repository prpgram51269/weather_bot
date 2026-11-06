from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a92c6c45ffb6'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        CREATE TABLE users (
            user_id BIGINT PRIMARY KEY,
            city VARCHAR(100)
        )
    """)

    op.execute("""
        CREATE TABLE weather_history (
            id SERIAL PRIMARY KEY,
            user_id BIGINT REFERENCES users(user_id) ON DELETE CASCADE,
            city VARCHAR(100),
            temperature DOUBLE PRECISION,
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        )
    """)

    op.execute("CREATE INDEX idx_weather_created_at ON weather_history(created_at)")


def downgrade() -> None:
    op.execute("DROP TABLE weather_history")
    op.execute("DROP TABLE users")