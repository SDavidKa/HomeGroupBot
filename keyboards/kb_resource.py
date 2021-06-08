from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

list_handlers_docs = list()

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

def notes_kb(count: int, list_length: int):
    global list_handlers_docs
    markup = InlineKeyboardMarkup()
    stop = count

    if 0 <= count <= 10:
        count = 0
    elif count > 10 and (count % 10) != 0:
        count = count - (count % 10)
    else:
        count = count - 10

    while count < stop:
        button_text = f"{count+1}"
        callback_data = f"doc_{count+1}"
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )
        list_handlers_docs.append(callback_data)
        count = count + 1

    if list_length == count and list_length > (count - 10) >= 0:
        markup.row(InlineKeyboardButton(text="<<", callback_data="prev"))
    elif list_length > count and (count - 10) == 0:
        markup.row(InlineKeyboardButton(text=">>", callback_data="next"))
    elif (list_length / 10) > 2:
        markup.row(
            InlineKeyboardButton(text="<<", callback_data="prev"),
            InlineKeyboardButton(text=">>", callback_data="next"))

    markup.row(InlineKeyboardButton(text="Вернуться к таблицам", callback_data="back_to_table_list"))

    return markup
