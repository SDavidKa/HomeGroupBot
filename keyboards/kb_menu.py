from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

# Группировка кнопок для Меню
menu_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton('Конспекты'),
        KeyboardButton('Расписание')
    ],
    [
        KeyboardButton('Лидерские курсы')
    ],
    [
        KeyboardButton('Пожертвование')
    ]
], resize_keyboard=True)