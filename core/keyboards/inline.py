from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

select_inline_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='button 1',
            callback_data='pressed 1'
        )
    ],
    [
        InlineKeyboardButton(
            text='button 2',
            callback_data='pressed 2'
        )
    ],
    [
        InlineKeyboardButton(
            text='url button',
            url='https://github.com/KonstBeliakov/aiogram_test'
        )
    ]
])