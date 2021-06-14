from app import bot, dp, admin_id
from aiogram.types import Message
from keyboards import kb_donate, kb_menu, kb_resource, kb_leadershipCourse
from modules import getAirtableData, getUserLogsFromMessage
from datetime import datetime

async def send_to_admin_start(dp):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")

# Первое приветствие пользователя
@dp.message_handler(commands=['start'])
async def startsMessage(message: Message):
    await message.answer("Выбери необходимый пункт в меню", reply_markup=kb_menu.menu_kb)
    print(await getUserLogsFromMessage(message))

# Возвращение к меню
@dp.message_handler(text='Вернуться в меню')
async def getMenu(message: Message):
    await message.answer("Выбери необходимый пункт в меню", reply_markup=kb_menu.menu_kb)
    print(await getUserLogsFromMessage(message))

# Переход в раздел "Материалы"
@dp.message_handler(text='Материалы')
async def getResources(message: Message):
    await message.answer("Здесь ты найдешь конспекты и другие материалы для домашних групп."
                         "\n\nВыбери раздел:", reply_markup=kb_resource.resource_kb)
    print(await getUserLogsFromMessage(message))

# Выдача расписания
@dp.message_handler(text='Расписание')
async def getScheduler(message: Message):
    data_from_airtable = await getAirtableData(message.text, 'Date_time_meeting')
    text = await getListOfEvents(data_from_airtable)
    await message.answer(text)
    print(await getUserLogsFromMessage(message))

# Выдача материалов лидерского курса
@dp.message_handler(text='Лидерские курсы')
async def getLeadershipCourse(message: Message):
    await message.answer("Здесь ты найдешь материалы для лидеров домашних групп:",
                         reply_markup=kb_leadershipCourse.leadershipCourse_kb)
    print(await getUserLogsFromMessage(message))

# Переход в раздел "Пожертвование"
@dp.message_handler(text='Пожертвовать')
async def getDonate(message: Message):
    await message.answer("Благодаря твоей поддержке мы можем" +
                         "\nпродолжать насаждать церкви и распространять Евангелие!" +
                         "\n\nВыбери, на то что ты пожертвуешь:", reply_markup=kb_donate.donate_kb)
    print(await getUserLogsFromMessage(message))

async def getListOfEvents(data: list):
    text = "Расписание ближайших мероприятий церкви в Москве:\n"
    pattern_in = "%Y-%m-%dT%H:%M:%S.%f%z"
    pattern_out = "%d.%m.%y %H:%M"
    date_now = datetime.now().strftime(pattern_out)
    check = True
    for note in data:
        date_meeting = datetime.strptime(note['fields']['Date_time_meeting'], pattern_in).strftime(pattern_out)
        if date_meeting > date_now:
            text += f"\n● {note['fields']['Name']} - {date_meeting}"
            check = False
    if check:
        text = "Пока что нет запланированных мероприятий"

    return text
