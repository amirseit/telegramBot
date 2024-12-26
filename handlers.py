import logging
from telegram import Update
from telegram.ext import ContextTypes

from db import add_user

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command."""
    if update.effective_chat is None:
        return
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello! I'm your Telegram bot. Here's what I can do:\n"
             "- Use /help to see available commands.\n"
             "- Use /register to subscribe to updates.\n"
             "- Ask about 'price' or 'support' to get more information.\n"
             "- Type 'catalog' to receive our catalog."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command."""
    if update.effective_chat is None:
        return
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Here are the commands you can use:\n"
             "/start - Start the bot\n"
             "/help - Get help\n"
             "/register - Subscribe to updates\n"
             "You can also ask about 'price', 'support', or 'catalog'."
    )

async def keyword_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Respond to specific keywords in user messages."""
    if not update.message or not update.message.text or not update.effective_chat:
        return  # Safeguard against None values

    user_message = update.message.text.lower()

    if "price" in user_message:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Our service costs $50/month."
        )
    elif "support" in user_message:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="You can reach our support team here: https://example.com/support"
        )
    elif "catalog" in user_message:
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo="https://i.etsystatic.com/28551648/r/il/c25e5c/4713717902/il_1140xN.4713717902_a68e.jpg",
            caption="Here is our catalog."
        )
    else:
        # Default response for unmatched messages
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="I'm sorry, I didn't understand that. Try asking about 'price' or 'support'."
        )  

async def register_user(update: Update, context: ContextTypes.DEFAULT_TYPE, db_pool):
    """Register a user in the database."""
    if update.effective_chat:
        chat_id = update.effective_chat.id
        username = update.effective_user.username if update.effective_user else None
        await add_user(db_pool, chat_id, username)
        await context.bot.send_message(
            chat_id=chat_id,
            text="You've been registered for updates!"
        )
