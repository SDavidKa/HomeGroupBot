from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Группировка кнопок для Пожертвовать
donate_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton('Пожертвовать'),
        KeyboardButton('Реквизиты')
    ],
    [
        KeyboardButton('Вернуться в меню')
    ]
], resize_keyboard=True)