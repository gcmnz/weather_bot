import asyncio
from time import strftime

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from weather import get_weather

TOKEN = 'not today'

bot = Bot(token=TOKEN)
dp = Dispatcher()

translate = {
    'january': 'января',
    'february': 'февраля',
    'march': 'марта',
    'april': 'апреля',
    'may': 'мая',
    'june': 'июня',
    'july': 'июля',
    'august': 'августа',
    'september': 'сентября',
    'october': 'октября',
    'november': 'ноября',
    'december': 'декабря'
}


@dp.message(Command('commands'))
async def commands(message: Message):
    answer = '/commands - команды\n/today - погода на сегодня\n/tomorrow - погода на завтра'

    await message.answer(answer)


@dp.message(Command('today'))
async def today_weather(message: Message):
    day = int(strftime('%d'))
    month = strftime('%B').lower()
    url = f'https://pogoda.mail.ru/prognoz/moskva/{day}-{month}/'
    result_answer = f'Погода на {day} {translate[month]}:'

    for i in get_weather(url):
        result_answer += f'\n{i}'

    await message.answer(result_answer)


@dp.message(Command('tomorrow'))
async def tomorrow_weather(message: Message):
    day = int(strftime('%d'))+1
    month = strftime('%B').lower()
    url = f'https://pogoda.mail.ru/prognoz/moskva/{day}-{month}/'
    result_answer = f'Погода на {day} {translate[month]}:'

    for i in get_weather(url):
        result_answer += f'\n{i}'

    await message.answer(result_answer)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
