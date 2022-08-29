from telegram import Bot as TelegramBot, Update
from telegram.ext import Dispatcher

from core.settings import TELEGRAM_BOT_TOKEN


def webhook_handler(data):
    bot = TelegramBot(TELEGRAM_BOT_TOKEN)
    dispatcher = Dispatcher(bot, None)

    update = Update.de_json(data, bot)
    # Update dispatcher process that handler to process this message
    dispatcher.process_update(update)
