from aiogram import Bot, Dispatcher, types, F
import asyncio
import logging
from aiogram.fsm.state import State
from aiogram.fsm.state import StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from config_reader import config

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.bot_token.get_secret_value())

dp = Dispatcher()
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message(F.text.lower() == 'рассчитать')
async def main_menu(message: types.Message):
    buttons = [
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')],
    ]

    kb = InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True, input_field_placeholder='Выберите')
    await message.answer('Выберите опцию: ', reply_markup= kb)

@dp.callback_query(F.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer('10 x вес (кг) + 6,25 х рост (см) - 5 х возраст (г) - 161')
    await call.answer()



@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    # buttons = [
    #     [KeyboardButton(text='Рассчитать')],
    #     [KeyboardButton(text='Информация')],
    # ]
    #
    # kb = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, input_field_placeholder='Выберите')
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.callback_query(F.data == 'calories')
async def set_age(call, state: FSMContext):
    await call.message.answer('Введите свой возраст')
    await state.set_state(UserState.age)
    await call.answer()

@dp.message(F.text.lower() == 'информация')
async def information(message: types.Message):
    await message.answer('Информация о боте', reply_markup=types.ReplyKeyboardRemove())

@dp.message(UserState.age)
async def set_growth(message, state):
    await state.update_data(age= int(message.text))
    await message.answer('Введите свой рост')
    await state.set_state(UserState.growth)


@dp.message(UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth= int(message.text))
    await message.answer('Введите свой вес')
    await state.set_state(UserState.weight)


@dp.message(UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight= int(message.text))
    data = await state.get_data()
    for_w = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] - 161
    await message.answer(f'Ваша норма каллорий: {for_w}', reply_markup=types.ReplyKeyboardRemove())


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())