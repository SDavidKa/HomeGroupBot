from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Группировка кнопок для Пожертвовать
donate_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton('Слово жизни'),
        KeyboardButton('Строим церковь')
    ],
    [
        KeyboardButton('Израиль'),
        KeyboardButton('Социальная работа')
    ],
    [
        KeyboardButton('Миссия: до края земли'),
        KeyboardButton('500 по 500')
    ],
    [
        KeyboardButton('Реквизиты'),
        KeyboardButton('Вернуться в меню')
    ]
], resize_keyboard=True)
