from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='help',
            description='Помощь'
        ),
        BotCommand(
            command='inline',
            description='Показать inline клавиатуру'
        ),
        BotCommand(
            command='form',
            description='Начать опрос'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
