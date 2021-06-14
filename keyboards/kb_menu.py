from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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
        KeyboardButton('Пожертвование')
    ]
], resize_keyboard=True)
