"""
@Jefffsmartbot - A smart Telegram bot
Deployed on Railway with GitHub integration
"""

import os
import logging
import sys
from datetime import datetime
from typing import Dict, Any

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

# ===== CONFIGURATION =====

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

# Environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", 8080))
ENVIRONMENT = os.getenv("ENVIRONMENT", "production")

# Validate required variables
if not BOT_TOKEN:
    logger.error("❌ BOT_TOKEN environment variable is required!")
    sys.exit(1)

logger.info(f"🚀 Starting @Jefffsmartbot in {ENVIRONMENT} mode...")


# ===== COMMAND HANDLERS =====

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /start command with a welcome message and inline keyboard."""
    user = update.effective_user
    first_name = user.first_name or "there"

    # Welcome message
    welcome_text = (
        f"👋 Hello {first_name}!\n\n"
        f"I'm **@Jefffsmartbot**, your intelligent assistant.\n"
        f"Here's what I can do for you:\n\n"
        f"📊 **Commands:**\n"
        f"• /start - Show this welcome message\n"
        f"• /help - Get detailed help\n"
        f"• /ping - Check if I'm alive\n"
        f"• /info - Bot information\n"
        f"• /time - Current server time\n"
        f"• /echo <text> - Echo your message back\n\n"
        f"💡 Just send me any text and I'll respond!\n"
        f"🛠️ More features coming soon..."
    )

    # Inline keyboard
    keyboard = [
        [
            InlineKeyboardButton("ℹ️ Help", callback_data="help"),
            InlineKeyboardButton("📊 Status", callback_data="status"),
        ],
        [
            InlineKeyboardButton("🌐 GitHub", url="https://github.com/yourusername/jefffsmartbot"),
            InlineKeyboardButton("📢 Channel", url="https://t.me/yourchannel"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        welcome_text,
        parse_mode="Markdown",
        reply_markup=reply_markup,
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /help command."""
    help_text = (
        f"📖 **Help & Commands**\n\n"
        f"**Available Commands:**\n"
        f"• /start - Start the bot\n"
        f"• /help - Show this help message\n"
        f"• /ping - Check bot status\n"
        f"• /info - Display bot info\n"
        f"• /time - Current server time\n"
        f"• /echo <text> - Echo your message\n\n"
        f"**Features:**\n"
        f"• ✨ Smart responses\n"
        f"• 🔒 Secure and private\n"
        f"• ⚡ Fast and reliable\n"
        f"• 🌐 Always online (24/7)\n\n"
        f"**Support:**\n"
        f"• GitHub: https://github.com/yourusername/jefffsmartbot\n"
        f"• Contact: @yourusername"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /ping command to check bot status."""
    start_time = datetime.now()
    await update.message.reply_text("🏓 Pinging...")
    elapsed = (datetime.now() - start_time).total_seconds()
    await update.message.reply_text(
        f"🏓 **Pong!**\n"
        f"• Response time: `{elapsed:.3f}s`\n"
        f"• Status: ✅ Online\n"
        f"• Uptime: 24/7\n"
        f"• Version: 1.0.0",
        parse_mode="Markdown",
    )


async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /info command."""
    info_text = (
        f"🤖 **Bot Information**\n\n"
        f"• **Name:** @Jefffsmartbot\n"
        f"• **Version:** 1.0.0\n"
        f"• **Environment:** {ENVIRONMENT}\n"
        f"• **Platform:** Railway + GitHub\n"
        f"• **Language:** Python 3.11+\n"
        f"• **Framework:** python-telegram-bot\n"
        f"• **Status:** 🟢 Active\n\n"
        f"**Created by:** @yourusername\n"
        f"**GitHub:** https://github.com/yourusername/jefffsmartbot"
    )
    await update.message.reply_text(info_text, parse_mode="Markdown")


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /time command."""
    now = datetime.now()
    time_str = now.strftime("%Y-%m-%d %H:%M:%S %Z")
    await update.message.reply_text(
        f"🕐 **Current Server Time**\n\n"
        f"`{time_str}`\n\n"
        f"Timezone: UTC",
        parse_mode="Markdown",
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user's message back with smart responses."""
    user_message = update.message.text
    user_name = update.effective_user.first_name or "User"

    # Smart responses
    smart_responses = {
        "hello": f"Hello {user_name}! 👋 How can I help you today?",
        "hi": f"Hi {user_name}! 👋 Good to see you!",
        "how are you": f"I'm doing great, {user_name}! 🤖 Thanks for asking!",
        "what is your name": f"I'm @Jefffsmartbot, your smart assistant! 🤖",
        "help": f"Type /help to see all my commands! 📖",
        "thanks": f"You're welcome, {user_name}! 😊",
        "thank you": f"My pleasure, {user_name}! 😊",
        "good morning": f"Good morning, {user_name}! ☀️ Have a great day!",
        "good night": f"Good night, {user_name}! 🌙 Sleep well!",
    }

    # Check for smart responses
    lower_message = user_message.lower().strip()
    for key, response in smart_responses.items():
        if key in lower_message:
            await update.message.reply_text(response)
            return

    # Default echo response
    echo_response = (
        f"📨 **You said:**\n"
        f"`{user_message}`\n\n"
        f"🤖 **My response:**\n"
        f"I received your message! Type /help to see what I can do."
    )
    await update.message.reply_text(echo_response, parse_mode="Markdown")


# ===== CALLBACK QUERY HANDLERS =====

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle inline keyboard button presses."""
    query = update.callback_query
    await query.answer()

    if query.data == "help":
        await query.edit_message_text(
            f"📖 **Help Section**\n\n"
            f"Type /help for a complete list of commands.\n"
            f"You can also just chat with me naturally! 💬",
            parse_mode="Markdown",
        )
    elif query.data == "status":
        now = datetime.now()
        await query.edit_message_text(
            f"📊 **Bot Status**\n\n"
            f"• Status: 🟢 Online\n"
            f"• Uptime: 24/7\n"
            f"• Response time: ⚡ Fast\n"
            f"• Current time: `{now.strftime('%H:%M:%S UTC')}`\n"
            f"• Users served: Growing! 📈",
            parse_mode="Markdown",
        )


# ===== ERROR HANDLER =====

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log errors and notify the user."""
    logger.error(f"Update {update} caused error {context.error}")

    # Notify the user
    try:
        if update and update.effective_message:
            await update.effective_message.reply_text(
                "❌ Something went wrong! Please try again later.\n"
                "If the issue persists, contact @yourusername"
            )
    except Exception as e:
        logger.error(f"Failed to send error message: {e}")


# ===== MAIN APPLICATION =====

def main() -> None:
    """Main function to run the bot."""
    try:
        # Create application using the correct builder pattern for Python 3.13
        application = Application.builder().token(BOT_TOKEN).build()
        
        # Add command handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("ping", ping))
        application.add_handler(CommandHandler("info", info_command))
        application.add_handler(CommandHandler("time", time_command))
        application.add_handler(CommandHandler("echo", echo))
        
        # Add callback query handler
        application.add_handler(CallbackQueryHandler(button_callback))
        
        # Add message handler for non-command messages
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
        
        # Add error handler
        application.add_error_handler(error_handler)
        
        # Start the bot using polling
        logger.info("📡 Bot is starting in POLLING mode...")
        application.run_polling(allowed_updates=Update.ALL_TYPES)
        
    except Exception as e:
        logger.error(f"❌ Failed to start bot: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
