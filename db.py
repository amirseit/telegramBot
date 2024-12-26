import asyncpg
import os

async def init_db():
    """Initialize the database connection pool."""
    db_pool = await asyncpg.create_pool(
        user=os.environ["DB_USER"],            # Will raise KeyError if not set
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"],
        host=os.environ["DB_HOST"],
        port=int(os.environ["DB_PORT"]),
    )
    return db_pool

async def add_user(db_pool, chat_id, username):
    """Add a user to the database."""
    async with db_pool.acquire() as conn:
        await conn.execute(
            """
            INSERT INTO users (chat_id, username)
            VALUES ($1, $2)
            ON CONFLICT (chat_id) DO NOTHING;
            """,
            chat_id,
            username,
        )

async def get_all_users(db_pool):
    """Retrieve all users from the database."""
    async with db_pool.acquire() as conn:
        rows = await conn.fetch("SELECT chat_id FROM users;")
    return [row["chat_id"] for row in rows]
