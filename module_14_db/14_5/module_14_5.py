from aiogram import Bot, Dispatcher, types, F
import asyncio
import logging
from aiogram.fsm.state import State
from aiogram.fsm.state import StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, FSInputFile, \
    ReplyKeyboardRemove

from config_reader import config
from crud_functions import get_all_products, is_included, add_user, initiate_db
from texts import start

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.bot_token.get_secret_value())

dp = Dispatcher()
initiate_db()
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


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
    buttons = [
        [KeyboardButton(text='Рассчитать')],
        [KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить')],
        [KeyboardButton(text='Регистрация')]
    ]

    kb = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, input_field_placeholder='Выберите')
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

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


@dp.message(F.text.lower() == 'купить')
async def det_buying_list(message: types.Message):

    get_all_products()
    print(get_all_products())
    buttons = [
        [InlineKeyboardButton(text='Продукт 1', callback_data='product_buying')],
        [InlineKeyboardButton(text='Продукт 2', callback_data='product_buying')],
        [InlineKeyboardButton(text='Продукт 3', callback_data='product_buying')],
        [InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')],

    ]

    kb = InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True, input_field_placeholder='Выберите')
    for i in range(5, 9):
        img = FSInputFile(f"{i}.jpeg")
        if i == 5:
            await message.answer(f'Название: {get_all_products()[0][1]} | Описание: {get_all_products()[0][2]}| Цена: {get_all_products()[0][3]}', callback_data="product_buying")
            await message.answer_photo(img)
        if i == 6:
            await message.answer(f'Название: {get_all_products()[1][1]} | Описание: {get_all_products()[1][2]}| Цена: {get_all_products()[1][3]}', callback_data="product_buying")
            await message.answer_photo(img)
        if i == 7:
            await message.answer(f'Название: {get_all_products()[2][1]} | Описание: {get_all_products()[2][2]}| Цена: {get_all_products()[2][2]}', callback_data="product_buying")
            await message.answer_photo(img)
        if i == 8:
            await message.answer(f'Название: {get_all_products()[3][1]} | Описание: {get_all_products()[3][3]} | Цена: {get_all_products()[3][3]}',
                                 callback_data="product_buying")
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=kb)

@dp.callback_query(F.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer('Вы успешно приобрели продукт', reply_markup=types.ReplyKeyboardRemove())


@dp.message(F.text.lower() == 'регистрация')
async def sign_up(message, state: FSMContext):
    await message.answer('Введите имя пользователя (только латинский алфавит): ')
    await state.set_state(RegistrationState.username)

@dp.message(RegistrationState.username)
async def set_username(message, state):
    if not is_included(message.text):
        await state.update_data(username=message.text)
        await message.answer('Введите свой email: ')
        await state.set_state(RegistrationState.email)
    else:
        await message.answer('Пользователь существует, введите другое имя')
        await state.set_state(RegistrationState.username)

@dp.message(RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await state.set_state(RegistrationState.age)

@dp.message(RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=int(message.text))
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer('Регистрация прошла успешно', reply_markup=types.ReplyKeyboardRemove())


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())