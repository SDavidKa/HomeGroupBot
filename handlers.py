from main import bot, dp
from aiogram.types import Message
from config import admin_id
from keyboards import resource_kb

async def send_to_admin_start(dp):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")

async def send_to_admin_shutdown(dp):
    await bot.send_message(chat_id=admin_id, text="Бот отключен")
# Первое приветствие пользователя
@dp.message_handler(commands=['start'])
async def startsMessage(message: Message):
    await message.answer("Выбери необходимый пункт в меню", reply_markup=resource_kb)

# Выдача конспектов
@dp.message_handler(lambda message: message.text == 'Конспекты')
async def getResources(message: Message):
    await message.answer("Пока тебе ничего не дам")

# Выдача расписания
@dp.message_handler(lambda message: message.text == 'Расписание')
async def getSchedule(message: Message):
    await message.answer("Ничего не знаю")

# Выдача материалов лидерского курса
@dp.message_handler(lambda message: message.text == 'Лидерские курсы')
async def getLeadershipCourse(message: Message):
    await message.answer("Пока можешь глядуть, что-то здесь: https://www.youtube.com/c/wolrustv/playlists")

# Пожертвование
@dp.message_handler(lambda message: message.text == 'Пожертвовать')
async def getDonate(message: Message):
    await message.answer("Пока пользуйся этим сайтом: https://wolrus.org/donate")

# Неизвестная команда
@dp.message_handler()
async def unknownCommands(message: Message):
    await message.reply("Незнаю такой команды. Выбери что-то из меню", reply_markup=resource_kb)
