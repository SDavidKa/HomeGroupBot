from app import dp, airtable_api_key, airtable_base_id
from aiogram.types import Message, InputFile, CallbackQuery
from keyboards import resource as rs
import airtable as at

table_state = {
    "table_name": "",
    "table_count": 3,
    "table_stop": 3,
    "table_data": dict(),
    "list_name": list(),
    "message_id": int
}
# Метод получения данных с AirTable
def getAirtableData(table_name: str):
    airtable = at.Airtable(airtable_base_id, table_name, airtable_api_key)
    return airtable.get_all()

# Метод вывода списка тем
def getListNotes(data: dict, table_name: str):
    global table_state
    answer = f"Выбери тему таблицы «{table_name}»:"
    text = ""
    table_state['table_name'] = table_name
    table_state['table_data'] = data
    counter = 0
    names = list()
    for note in data:
        names.append(note['fields']['Name'])

    stop = counter + 3
    while counter < stop:
        text += f"\n{counter + 1}) {names[counter]}"
        counter += 1

    table_state['table_count'] = counter
    table_state['list_name'] = names

    return answer + text

# Метод перелистывания списка тем вперед
async def getNextListNotes(table_name: str, call: CallbackQuery):
    global table_state
    answer = f"Выбери тему таблицы «{table_name}»:"
    text = ""
    names = table_state['list_name']
    counter = table_state['table_count']

    if len(names) >= (counter + 3) > 0:
        stop = counter + 3

        while counter < stop:
            text += f"\n{counter + 1}) {names[counter]}"
            counter += 1

    else:
        while counter < len(names):
            text += f"\n{counter + 1}) {names[counter]}"
            counter += 1

    table_state['table_count'] = counter

    if counter >= len(names):
        await call.answer(text="Конец списка")

    return answer + text

# Метод перелистывания списка тем назад
async def getPreviousListNotes(table_name: str, call: CallbackQuery):
    global table_state
    answer = f"Выбери тему таблицы «{table_name}»:"
    text = ""
    names = table_state['list_name']
    if table_state['table_count'] >= 6:
        counter = table_state['table_count'] - 6
    elif len(names) % table_state['table_count'] or table_state['table_count'] == 5:
        counter = 0
    else:
        counter = table_state['table_count'] - 3

    if (counter + 3) > 0:
        stop = counter + 3

        while counter < stop:
            text += f"\n{counter + 1}) {names[counter]}"
            counter += 1
    else:
        while counter < len(names):
            text += f"\n{counter + 1}) {names[counter]}"
            counter += 1

    table_state['table_count'] = counter
    if counter == 3:
        await call.answer(text="Начало списка")

    return answer + text

# Метод вывода ссылки на документ
def getLinkDocumentFromNotes(call: CallbackQuery):
    global table_state
    data = getAirtableData(table_state['table_name'])
    counter = table_state['table_count'] - 2
    link = ""
    name = ""
    message = call.message.text

    names = message.split("\n")
    names.pop(0)

    if call.data == "first":
        for n in names:
            if not (n.find(f"{counter})")):
                new_name = n.split(f"{counter}) ")
                new_name.pop(0)
                name = new_name[0]
        for note in data:
            if note['fields']['Name'] == name:
                link = note['fields']['Attachments'][0]['url']
    elif call.data == "second":
        counter = counter + 1
        for n in names:
            if not (n.find(f"{counter})")):
                new_name = n.split(f"{counter}) ")
                new_name.pop(0)
                name = new_name[0]
        for note in data:
            if note['fields']['Name'] == name:
                link = note['fields']['Attachments'][0]['url']
    elif call.data == "third":
        counter = counter + 2
        for n in names:
            if not (n.find(f"{counter})")):
                new_name = n.split(f"{counter}) ")
                new_name.pop(0)
                name = new_name[0]
        for note in data:
            if note['fields']['Name'] == name:
                link = note['fields']['Attachments'][0]['url']
    return link

# Выдача конспектов воскресной проповеди
@dp.message_handler(text='Вс. проповеди')
async def getPreaching(message: Message):
    await message.answer("Тема 1\nНазвание конспекта 1")
    table_state['message_id'] = message.message_id

# Выдача конспектов
@dp.message_handler(text='Конспекты')
async def getNotes(message: Message):
    await message.answer("Выбери таблицу", reply_markup=rs.notes_menu_kb)
    table_state['message_id'] = message.message_id

@dp.callback_query_handler(text="Главные документы")
async def getNotesFromTableMainDocs(call: CallbackQuery):
    data_from_airtable = getAirtableData(call.data)
    text = getListNotes(data_from_airtable, call.data)
    await call.message.edit_text(text, reply_markup=rs.notes_kb)

@dp.callback_query_handler(text="Гостеприимство")
async def getNotesFromTableMainDocs(call: CallbackQuery):
    data_from_airtable = getAirtableData(call.data)
    text = getListNotes(data_from_airtable, call.data)
    await call.message.edit_text(text, reply_markup=rs.notes_kb)

@dp.callback_query_handler(text="Конспекты с ДГ")
async def getNotesFromTableMainDocs(call: CallbackQuery):
    data_from_airtable = getAirtableData(call.data)
    text = getListNotes(data_from_airtable, call.data)
    await call.message.edit_text(text, reply_markup=rs.notes_kb)

@dp.callback_query_handler(text="Книги для обязательного прочтения")
async def getNotesFromTableMainDocs(call: CallbackQuery):
    data_from_airtable = getAirtableData(call.data)
    text = getListNotes(data_from_airtable, call.data)
    await call.message.edit_text(text, reply_markup=rs.notes_kb)

@dp.callback_query_handler(text="обучающие аудио для лидеров")
async def getNotesFromTableMainDocs(call: CallbackQuery):
    data_from_airtable = getAirtableData(call.data)
    text = getListNotes(data_from_airtable, call.data)
    await call.message.edit_text(text, reply_markup=rs.notes_kb)

@dp.callback_query_handler(text="конспекты для окружных лидеров")
async def getNotesFromTableMainDocs(call: CallbackQuery):
    data_from_airtable = getAirtableData(call.data)
    text = getListNotes(data_from_airtable, call.data)
    await call.message.edit_text(text, reply_markup=rs.notes_kb)

@dp.callback_query_handler(text="first")
async def getFirstNotesFiles(call: CallbackQuery):
    await call.message.answer_document(InputFile.from_url(getLinkDocumentFromNotes(call)), caption="Вот твой документ")
    await call.message.answer(getListNotes(table_state['table_data'], table_state['table_name']), reply_markup=rs.notes_kb)
    await call.message.delete()

@dp.callback_query_handler(text="second")
async def getSecondNotesFiles(call: CallbackQuery):
    await call.message.answer_document(InputFile.from_url(getLinkDocumentFromNotes(call)), caption="Вот твой документ")
    await call.message.answer(getListNotes(table_state['table_data'], table_state['table_name']), reply_markup=rs.notes_kb)
    await call.message.delete()

@dp.callback_query_handler(text="third")
async def getThirdNotesFiles(call: CallbackQuery):
    await call.message.answer_document(InputFile.from_url(getLinkDocumentFromNotes(call)), caption="Вот твой документ")
    await call.message.answer(getListNotes(table_state['table_data'], table_state['table_name']), reply_markup=rs.notes_kb)
    await call.message.delete()

@dp.callback_query_handler(text="prev")
async def getPreviousNotesLists(call: CallbackQuery):
    text = await getPreviousListNotes(table_state['table_name'], call)
    await call.message.edit_text(text, reply_markup=rs.notes_kb)

@dp.callback_query_handler(text="next")
async def getNextNotesLists(call: CallbackQuery):
    text = await getNextListNotes(table_state['table_name'], call)
    await call.message.edit_text(text, reply_markup=rs.notes_kb)

@dp.callback_query_handler(text="back_to_table_list")
async def getNextNotesLists(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_text("Выбери таблицу", reply_markup=rs.notes_menu_kb)
