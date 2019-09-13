import os
from datetime import date, timedelta

from src.crawler import get_posts
from src.bot import configure_telegram
from src.models import Chat


def deliver(event, context):
    bot = configure_telegram()
    chats = Chat.scan()
    yesterday = date.today() - timedelta(days=1)
    texts = get_posts(yesterday)

    for chat in chats:
        for text in texts:
            bot.send_message(chat_id=chat.chat_id, text=text)
