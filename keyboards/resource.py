from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from app import airtable

# Группировка кнопок для Материалы
resource_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton('Конспекты'),
        KeyboardButton('Вс. проповеди')
    ],
    [
        KeyboardButton('Вернуться в меню')
    ]
], resize_keyboard=True)

notesName_kb = InlineKeyboardMarkup()
data = airtable.get_all()
for note in data:
    name = note['fields']['Name']
    url = note['fields']['Attachments'][0]['url']
    notesName_kb.insert(InlineKeyboardButton(text=name, url=url))