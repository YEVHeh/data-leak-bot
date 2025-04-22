import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = os.getenv("BOT_TOKEN")  # використовуй тільки одну змінну

if not API_TOKEN:
    raise ValueError("BOT_TOKEN is not set!")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome! Send me your email to check for leaks.")

if __name__ == '__main__':
    executor.start_polling(dp)
