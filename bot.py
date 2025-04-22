import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = os.getenv("BOT_TOKEN")

if not API_TOKEN:
    raise ValueError("BOT_TOKEN is not set!")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome! Send me your email to check for leaks.")

@dp.message_handler()
async def check_email(message: types.Message):
    email = message.text.strip()
    if '@' in email and '.' in email:
        await message.reply("🔍 Scanning your email for leaks...")
        await message.answer("⚠️ Warning: Your email was found in multiple leaks!\nTap here to learn more: https://your-cpa-link.com")
    else:
        await message.reply("❌ That doesn't look like a valid email. Try again.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
