import json
import telegram
import os

from src.logger import logger
from src.response import OK_RESPONSE, ERROR_RESPONSE
from src.bot import configure_telegram
from src.models import Chat
from pynamodb.exceptions import DoesNotExist


def webhook(event, context):
    """
    Reply to input message (only /start)
    """

    bot = configure_telegram()
    logger.info('Event: {}'.format(event))

    if event.get('body'):
        logger.info('Message received')
        update = telegram.Update.de_json(json.loads(event.get('body')), bot)
        chat_id = update.message.chat.id
        text = update.message.text

        if text == '/start':
            try:
                Chat.get(chat_id)
            except DoesNotExist:
                chat = Chat(chat_id)
                chat.save()
                reply_text = """카이스트 아라의 Food 게시판 업데이트 알림 봇입니다. 매일 오전 11시에 전날의 게시글이 전달됩니다."""
                bot.send_message(chat_id=chat_id, text=reply_text)
                logger.info('Message sent')
            else:
                logger.info('Input message ignored')
        else:
            logger.info('Input message ignored')

        return OK_RESPONSE

    return ERROR_RESPONSE


def set_webhook(event, context):
    """
    Sets the Telegram bot webhook.
    """

    logger.info('Event: {}'.format(event))
    bot = configure_telegram()
    url = 'https://{}/{}/'.format(
        event.get('headers').get('Host'),
        event.get('requestContext').get('stage'),
    )
    webhook = bot.set_webhook(url)

    if webhook:
        return OK_RESPONSE

    return ERROR_RESPONSE
