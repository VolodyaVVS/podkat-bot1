import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton("➕ Новая аренда подката 1"))
menu.add(KeyboardButton("➕ Новая аренда подката 2"))
menu.add(KeyboardButton("📋 История аренд"))

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("Привет! Выберите действие:", reply_markup=menu)

@dp.message_handler(lambda message: message.text == "➕ Новая аренда подката 1")
async def new_rental1(message: types.Message):
    await message.answer("Аренда подката №1 добавлена.")

@dp.message_handler(lambda message: message.text == "➕ Новая аренда подката 2")
async def new_rental2(message: types.Message):
    await message.answer("Аренда подката №2 добавлена.")

@dp.message_handler(lambda message: message.text == "📋 История аренд")
async def history(message: types.Message):
    await message.answer("Здесь будет история аренд.")

if __name__ == "__main__":
    executor.start_polling(dp)
