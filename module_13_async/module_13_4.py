from aiogram import Bot, Dispatcher, types
import asyncio
import logging
from aiogram.fsm.state import State
from aiogram.fsm.state import StatesGroup
from aiogram.fsm.context import FSMContext

from config_reader import config

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.bot_token.get_secret_value())

dp = Dispatcher()
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(lambda message: message.text == 'Calories')
async def set_age(message, state: FSMContext):
    await message.answer('Введите свой возраст')
    await state.set_state(UserState.age)

@dp.message(UserState.age)
async def set_growth(message, state):
    await state.update_data(age= int(message.text))
    await message.answer('Введите свой рост')
    await state.set_state(UserState.growth)
    # await message.answer(f'Доставка будет отправлена на {data['first']}')


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
    await message.answer(f'Ваша норма каллорий: {for_w}')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())