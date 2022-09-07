from telegram import Update
from telegram.ext import ContextTypes

from app.users.models import User


def start(update: Update, context: ContextTypes):
    chat_id = update.message.chat_id
    user = update.message.from_user
    _, created = User.objects.get_or_create(
        chat_id=chat_id,
        defaults={
            "username": user.username,
            "first_name": user.first_name,
        },
    )
    context.bot.send_message(
        chat_id,
        f"Hello {user.first_name}, Is new user: {created}",
    )
