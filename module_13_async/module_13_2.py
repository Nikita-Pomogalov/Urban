from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio
import logging
from aiogram.enums.dice_emoji import DiceEmoji
from datetime import datetime

from config_reader import config

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.bot_token.get_secret_value())

dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    print('Привет! Я бот, помогающий твоему здоровью.')
    await message.answer('Привет! Я бот, помогающий твоему здоровью.')

@dp.message()
async def cmd_test2(message: types.Message):
    print('Введите команду /start, чтобы начать общение')
    await message.answer("Введите команду /start, чтобы начать общение")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())