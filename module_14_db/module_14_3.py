from aiogram import Bot, Dispatcher, types, F
import asyncio
import logging
from aiogram.fsm.state import State
from aiogram.fsm.state import StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, FSInputFile

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
    buttons = [
        [KeyboardButton(text='Рассчитать')],
        [KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить')]
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
            await message.answer(f'Название: Конфеты «Самый умный» | Описание: Конфета из легкой стаивающей глазури с н'
                                 f'ачинкой из нежнейшего молочного крема. Начинка изготовлена из большого количества мол'
                                 f'ока и содержит кальций | Цена: 60р/100г', callback_data="product_buying")
            await message.answer_photo(img)
        if i == 6:
            await message.answer(f'Название: Конфеты Fruit Story | Описание: Жевательные конфеты.   Ассорти вкусов:'
                                 f'лимон, смородина, малина и ананас | Цена: 256р/1кг', callback_data="product_buying")
            await message.answer_photo(img)
        if i == 7:
            await message.answer(f'Название: Конфеты Славянка Левушка | Описание: Желеобразная начинка с мягкой'
                                 f'карамелью в сочетании с шоколадной глазурью – такое лакомство побьет все рекорды '
                                 f'популярности.| Цена: 571р/1кг', callback_data="product_buying")
            await message.answer_photo(img)
        if i == 8:
            await message.answer(f'Название: Конфеты Яшкино Чио Рио | Описание: Чио Рио это любимая многими сладкоежками'
                                 f'конфета. Начинка из пралине с добавлением бисквитных, хрустящих шариков под слоем'
                                 f'золотистой карамели. Шоколадная глазурь полностью покрывает эту сладость. Обертка, '
                                 f'выполненная в японском стиле с нежными цветами Сакуры. | Цена: 500р/1кг',
                                 callback_data="product_buying")
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=kb)

@dp.callback_query(F.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer('Вы успешно приобрели продукт', reply_markup=types.ReplyKeyboardRemove() )

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())