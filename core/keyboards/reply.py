from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Ряд 1 Кнопка 1'
        ),
        KeyboardButton(
            text='Ряд 1 Кнопка 2'
        ),
        KeyboardButton(
            text='Ряд 1 Кнопка 3'
        ),
    ],
    [
        KeyboardButton(
            text='Ряд 2 Кнопка 1'
        ),
        KeyboardButton(
            text='Ряд 2 Кнопка 2'
        ),
        KeyboardButton(
            text='Ряд 2 Кнопка 3'
        ),
        KeyboardButton(
            text='Ряд 2 Кнопка 4'
        ),
    ]
], resize_keyboard=True,
    one_time_keyboard=True,  # клавиатура будет скрыта после одного нажатия
    input_field_placeholder='Выбери одну из кнопок',  # подсказка для пользователя в поле ввода сообщения
    selective=True  # показать клавиатуру только тому, кто ее запросил (актуально только для групповых чатов)
)

loc_tel_poll_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Отправить геолокацию',
            request_location=True
        ),
        KeyboardButton(
            text='Отправить номер телефона',
            request_contact=True
        )
    ],
    [
        KeyboardButton(
            text='Создать викторину',
            request_poll=KeyboardButtonPollType()
            # type='quiz' - викторина; type='regular' - опрос с несколькими вариантаи ответа
        )
    ],
], resize_keyboard=True, one_time_keyboard=False,
    input_field_placeholder='Отправь локацию, номер телефона или создай викторину/опрос'
)


def get_reply_keyboard():  # используем другой тип создания клавиатуры
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='Кнопка 1')
    keyboard_builder.button(text='Кнопка 2')
    keyboard_builder.button(text='Кнопка 3')

    keyboard_builder.button(text='Отправить геолокацию', request_location=True)
    keyboard_builder.button(text='Отправить номер телефона', request_contact=True)
    keyboard_builder.button(text='Создать викторину', request_poll=KeyboardButtonPollType())

    keyboard_builder.adjust(3, 2, 1)  # указываем количество кнопок в рядах

    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True,
                                      input_field_placeholder='Выбери одну из кнопок')
