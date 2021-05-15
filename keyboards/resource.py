from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaDocument

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

notes_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Главные документы", callback_data="Главные документы"),
        InlineKeyboardButton(text="Гостеприимство", callback_data="Гостеприимство")
    ],
    [
        InlineKeyboardButton(text="Конспекты с ДГ", callback_data="Конспекты с ДГ"),
        InlineKeyboardButton(text="Книги", callback_data="Книги для обязательного прочтения")

    ],
    [
        InlineKeyboardButton(text="Обучающее аудио", callback_data="обучающие аудио для лидеров"),
        InlineKeyboardButton(text="Конспекты для окружных лидеров", callback_data="конспекты для окружных лидеров")

    ]
])

notes_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="1", callback_data="first"),
        InlineKeyboardButton(text="2", callback_data="second"),
        InlineKeyboardButton(text="3", callback_data="third")
    ],
    [
        InlineKeyboardButton(text="<<", callback_data="prev"),
        InlineKeyboardButton(text=">>", callback_data="next")
    ],
    [
        InlineKeyboardButton(text="Вернуться к таблицам", callback_data="back_to_table_list")
    ]
])

# count = 1
# ulrsDocument = ['urls']

# for note in data:
#     name = note['fields']['Name']
#     url = note['fields']['Attachments'][0]['url']
#     if(note['fields']['Attachments'][0]['type'] == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'):
#         notesName_kb.insert(InlineKeyboardButton(text=name, callback_data=f'inputFile_{count}'))
#         count = count + 1
#         ulrsDocument.append(url)
#     else:
#         notesName_kb.insert(InlineKeyboardButton(text=name, url=url))