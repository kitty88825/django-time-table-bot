from telegram import Update
from telegram.ext import ContextTypes


def start(update: Update, context: ContextTypes):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id, f"Hello {update.message.from_user.first_name}")
