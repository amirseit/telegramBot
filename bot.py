import asyncio
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os

# Import handlers
from handlers import start, help_command, keyword_reply, register_user

# Import scheduler
from scheduler import schedule_broadcasts

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set in the environment variables")

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

scheduler_task = None  # Global reference for the scheduler task


from db import init_db, get_all_users, add_user

async def post_init(application):
    """Callback to start the scheduler and initialize the database."""
    global scheduler_task, db_pool
    logger.info("Initializing database...")
    db_pool = await init_db()

    logger.info("Starting the scheduler...")
    scheduler_task = application.create_task(
        schedule_broadcasts(application, db_pool)
    )


async def on_shutdown(application):
    """Callback to gracefully shutdown running tasks."""
    global scheduler_task
    logger.info("Shutting down tasks...")
    if scheduler_task:
        scheduler_task.cancel()
        try:
            await scheduler_task
        except asyncio.CancelledError:
            logger.info("Scheduler task cancelled successfully.")
    logger.info("Shutdown complete.")


if __name__ == "__main__":
    # Create the bot application
    application = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .post_init(post_init)  # Use post_init to start the scheduler
        .post_shutdown(on_shutdown)  # Use post_shutdown for cleanup
        .build()
    )

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("register", lambda update, context: register_user(update, context, db_pool)))

    # Add message handlers
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, keyword_reply))

    # Start the bot
    logger.info("Starting the bot...")
    application.run_polling()
