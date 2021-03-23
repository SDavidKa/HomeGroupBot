from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

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