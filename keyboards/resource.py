from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaDocument
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
count = 1
ulrsDocument = ['urls']

for note in data:
    name = note['fields']['Name']
    url = note['fields']['Attachments'][0]['url']
    if(note['fields']['Attachments'][0]['type'] == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'):
        notesName_kb.insert(InlineKeyboardButton(text=name, callback_data=f'inputFile_{count}'))
        count = count + 1
        ulrsDocument.append(url)
    else:
        notesName_kb.insert(InlineKeyboardButton(text=name, url=url))