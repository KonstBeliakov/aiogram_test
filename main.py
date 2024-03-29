from aiogram import Bot, Dispatcher
from aiogram.types import Message, ContentType

import asyncio
import logging
import os

from core.handlers.basic import get_started, get_photo, get_hello, get_inline
from core.settings import settings
from aiogram.filters import ContentTypesFilter, Command
from aiogram import F
from core.handlers.basic import get_location
from core.utils.commands import set_commands
from core.handlers import form
from core.utils.statesform import StepsForm

admin_id = []


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - [%(levelname)s] - %(name)s -'
                               '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')

    bot = Bot(token=settings.bots.bot_token)

    dp = Dispatcher()
    dp.message.register(get_started, Command(commands=['start', 'run']))
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_hello, F.text == 'Привет')
    #dp.message.register(get_photo, ContentTypesFilter(content_types=[ContentType.PHOTO]))
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_location, ContentTypesFilter(content_types=[ContentType.LOCATION]))
    dp.message.register(get_inline, Command(commands='inline'))
    dp.message.register(form.get_form, Command(commands='form'))
    dp.message.register(form.get_name, StepsForm.GET_NAME)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
