from aiogram import Bot
from aiogram.types import Message

import json


async def get_started(message: Message, bot: Bot):
    # можно написать в любой чат
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}')

    # ответить в том же чате
    await message.answer(f'Привет {message.from_user.first_name}. Рад тебя видеть!')

    # ответ на сообщение пользователя
    await message.reply(f'Привет {message.from_user.first_name}. Рад тебя видеть!')


async def get_photo(message: Message, bot: Bot):
    await message.answer('Сохраню эту картинку')

    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')


async def get_hello(message: Message, bot: Bot):
    await message.answer('И тебе привет!')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)
