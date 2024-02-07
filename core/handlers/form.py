from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statesform import StepsForm


async def get_form(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}Начинаем заполнять анкету. Напиши, пожалуйста, свое имя')
    await state.set_state(StepsForm.GET_NAME)


async def get_name(message:Message, state: FSMContext):
    await message.answer(f'Твое имя:\r\n{message.text}\r\nТеперь, введи фамилию')
    await state.update_data(name=message.text)
    await state.set_state(StepsForm.GET_LAST_NAME)
