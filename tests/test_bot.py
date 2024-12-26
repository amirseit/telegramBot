import pytest
from unittest.mock import AsyncMock, MagicMock
from telegram import Update
from telegram.ext import ContextTypes
from handlers import start, help_command, keyword_reply, register_user


@pytest.mark.asyncio
async def test_start_command():
    """Test the /start command."""
    # Mock update and context
    update = AsyncMock(spec=Update)
    context = MagicMock()  # Use MagicMock for ContextTypes
    context.bot = AsyncMock()  # Mock the bot attribute

    update.effective_chat.id = 12345  # Mock chat ID

    await start(update, context)

    context.bot.send_message.assert_called_once_with(
        chat_id=12345,
        text=(
            "Hello! I'm your Telegram bot. Here's what I can do:\n"
            "- Use /help to see available commands.\n"
            "- Use /register to subscribe to updates.\n"
            "- Ask about 'price' or 'support' to get more information.\n"
            "- Type 'catalog' to receive our catalog."
        )
    )


@pytest.mark.asyncio
async def test_help_command():
    """Test the /help command."""
    update = AsyncMock(spec=Update)
    context = MagicMock()
    context.bot = AsyncMock()

    update.effective_chat.id = 12345

    await help_command(update, context)

    context.bot.send_message.assert_called_once_with(
        chat_id=12345,
        text=(
            "Here are the commands you can use:\n"
            "/start - Start the bot\n"
            "/help - Get help\n"
            "/register - Subscribe to updates\n"
            "You can also ask about 'price', 'support', or 'catalog'."
        )
    )



@pytest.mark.asyncio
async def test_keyword_reply_price():
    """Test the 'price' keyword response."""
    update = AsyncMock(spec=Update)
    context = MagicMock()
    context.bot = AsyncMock()

    update.message.text = "What is the price?"
    update.effective_chat.id = 12345

    await keyword_reply(update, context)

    context.bot.send_message.assert_called_once_with(
        chat_id=12345,
        text="Our service costs $50/month."
    )


@pytest.mark.asyncio
async def test_keyword_reply_support():
    """Test the 'support' keyword response."""
    update = AsyncMock(spec=Update)
    context = MagicMock()
    context.bot = AsyncMock()

    update.message.text = "I need support"
    update.effective_chat.id = 12345

    await keyword_reply(update, context)

    context.bot.send_message.assert_called_once_with(
        chat_id=12345,
        text="You can reach our support team here: https://example.com/support"
    )


@pytest.mark.asyncio
async def test_keyword_reply_catalog():
    """Test the 'catalog' keyword response."""
    update = AsyncMock(spec=Update)
    context = MagicMock()
    context.bot = AsyncMock()

    update.message.text = "Show me the catalog"
    update.effective_chat.id = 12345

    await keyword_reply(update, context)

    context.bot.send_photo.assert_called_once_with(
        chat_id=12345,
        photo="https://i.etsystatic.com/28551648/r/il/c25e5c/4713717902/il_1140xN.4713717902_a68e.jpg",
        caption="Here is our catalog."
    )
