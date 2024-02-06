from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

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
],  resize_keyboard=True,
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
            request_poll=KeyboardButtonPollType() # type='quiz' - викторина; type='regular' - опрос с несколькими вариантаи ответа
        )
    ],
],  resize_keyboard=True, one_time_keyboard=False,
    input_field_placeholder='Отправь локацию, номер телефона или создай викторину/опрос'
)