from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

# Группировка кнопок для Пожертвовать
donate_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton('Строим церковь'),
        KeyboardButton('Израиль')
    ],
    [
        KeyboardButton('500 по 500'),
        KeyboardButton('Слово жизни')
    ],
    [
        KeyboardButton('До края земли'),
        KeyboardButton('Реквизиты')
    ],
    [
        KeyboardButton('Вернуться в меню')
    ]
], resize_keyboard=True)