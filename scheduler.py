import asyncio
from telegram.ext import Application
import logging

from db import get_all_users

logger = logging.getLogger(__name__)

async def broadcast_message(bot, registered_users: set):
    """Broadcast a message to all registered users."""
    for user_id in registered_users:
        try:
            await bot.send_message(
                chat_id=user_id,
                text="This is a scheduled broadcast message!"
            )
        except Exception as e:
            logger.error(f"Error sending message to {user_id}: {e}")

async def schedule_broadcasts(application, db_pool):
    """Broadcast messages periodically to users in the database."""
    while True:
        users = await get_all_users(db_pool)
        for user_id in users:
            try:
                await application.bot.send_message(
                    chat_id=user_id,
                    text="This is a scheduled broadcast message!"
                )
            except Exception as e:
                logger.error(f"Error sending message to {user_id}: {e}")
        await asyncio.sleep(10)  # Adjust interval as needed

def start_scheduler(application: Application, registered_users: set):
    """Start the asyncio scheduler."""
    application.create_task(schedule_broadcasts(application, registered_users))
