from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

# Группировка кнопок для Меню
menu_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton('Материалы'),
        KeyboardButton('Расписание')
    ],
    [
        KeyboardButton('Лидерские курсы')
    ],
    [
        KeyboardButton('Пожертвовать')
    ]
], resize_keyboard=True)