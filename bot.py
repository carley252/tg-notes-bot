n = 5

for i in range(1, n+1, -1):
    spaces = ' ' * (i - 1)
    stars = '*' * (n - i + 1 )
    print(spaces+stars)
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "8354737608:AAH_0Q1OyTWwk8jJj4Wc4lGc4syH-JJMUTc"  # сюда вставь свой токен

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    if message.text.lower() == "привет":
        await message.reply("Привет! Я бот!")
    elif message.text.lower() == "выход":
        await message.reply("Пока!")
        await bot.close()

if __name__ == "__main__":
    executor.start_polling(dp)
