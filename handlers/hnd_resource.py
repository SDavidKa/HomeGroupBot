from app import dp, airtable_api_key, airtable_base_id
from aiogram.types import Message, InputFile, CallbackQuery
from keyboards import kb_resource as rs
from asgiref.sync import sync_to_async
import airtable

# Глобальная переменная
table_state = dict()

# Метод получения данных с AirTable
async def getAirtableData(table_name: str):
    table = await sync_to_async(airtable.Airtable)(airtable_base_id, table_name, airtable_api_key)
    return table.get_all()

# Метод вывода списка тем
async def getListNotes(data: dict, table_name: str, call: CallbackQuery):
    global table_state
    answer = f"Выбери тему таблицы «{table_name}»:"
    text = ""
    counter = 0
    names = list()
    for note in data:
        names.append(note['fields']['Name'])

    stop = counter + 3
    while counter < stop:
        text += f"\n{counter + 1}) {names[counter]}"
        counter += 1

    table_state.update(user_id=call.from_user.id)
    table_state[call.from_user.id] = {
        'table_name': table_name,
        'table_data': data,
        'table_count': counter,
        'list_name': names
    }

    return answer + text

# Метод перелистывания списка тем вперед
async def getNextListNotes(call: CallbackQuery):
    global table_state
    answer = f"Выбери тему таблицы «{table_state[call.from_user.id]['table_name']}»:"
    text = ""
    names = table_state[call.from_user.id]['list_name']
    counter = table_state[call.from_user.id]['table_count']

    if len(names) >= (counter + 3) > 0:
        stop = counter + 3

        while counter < stop:
            text += f"\n{counter + 1}) {names[counter]}"
            counter += 1

    else:
        while counter < len(names):
            text += f"\n{counter + 1}) {names[counter]}"
            counter += 1

    table_state[call.from_user.id]['table_count'] = counter

    if counter >= len(names):
        await call.answer(text="Конец списка")

    return answer + text

# Метод перелистывания списка тем назад
async def getPreviousListNotes(call: CallbackQuery):
    global table_state
    answer = f"Выбери тему таблицы «{table_state[call.from_user.id]['table_name']}»:"
    text = ""
    names = table_state[call.from_user.id]['list_name']
    counter = table_state[call.from_user.id]['table_count']
    if counter >= 6:
        counter = counter - 6
    elif len(names) % counter or counter == 5:
        counter = 0
    else:
        counter = counter - 3

    if (counter + 3) > 0:
        stop = counter + 3

        while counter < stop:
            text += f"\n{counter + 1}) {names[counter]}"
            counter += 1
    else:
        while counter < len(names):
            text += f"\n{counter + 1}) {names[counter]}"
            counter += 1

    table_state[call.from_user.id]['table_count'] = counter
    if counter == 3:
        await call.answer(text="Начало списка")

    return answer + text

# Метод вывода ссылки на документ
async def getLinkDocumentFromNotes(call: CallbackQuery):
    global table_state
    data = await getAirtableData(table_state[call.from_user.id]['table_name'])
    counter = table_state[call.from_user.id]['table_count'] - 2
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

# Выдача конспектов
@dp.message_handler(text='Конспекты')
async def getNotes(message: Message):
    await message.answer("Выбери таблицу", reply_markup=rs.notes_menu_kb)
    table_state['message_id'] = message.message_id

@dp.callback_query_handler(text="Главные документы")
async def getNotesFromTableMainDocs(call: CallbackQuery):
    data_from_airtable = await getAirtableData(call.data)
    text = await getListNotes(data_from_airtable, call.data, call)
    await call.message.edit_text(text, reply_markup=rs.notes_kb)

@dp.callback_query_handler(text="Гостеприимство")
async def getNotesFromTableMainDocs(call: CallbackQuery):
    data_from_airtable = await getAirtableData(call.data)
    text = await getListNotes(data_from_airtable, call.data, call)
    await call.message.edit_text(text, reply_markup=rs.notes_kb)

@dp.callback_query_handler(text="Конспекты с ДГ")
async def getNotesFromTableMainDocs(call: CallbackQuery):
    data_from_airtable = await getAirtableData(call.data)
    text = await getListNotes(data_from_airtable, call.data, call)
    await call.message.edit_text(text, reply_markup=rs.notes_kb)

@dp.callback_query_handler(text="Книги для обязательного прочтения")
async def getNotesFromTableMainDocs(call: CallbackQuery):
    data_from_airtable = await getAirtableData(call.data)
    text = await getListNotes(data_from_airtable, call.data, call)
    await call.message.edit_text(text, reply_markup=rs.notes_kb)

@dp.callback_query_handler(text="обучающие аудио для лидеров")
async def getNotesFromTableMainDocs(call: CallbackQuery):
    data_from_airtable = await getAirtableData(call.data)
    text = await getListNotes(data_from_airtable, call.data, call)
    await call.message.edit_text(text, reply_markup=rs.notes_kb)

@dp.callback_query_handler(text="конспекты для окружных лидеров")
async def getNotesFromTableMainDocs(call: CallbackQuery):
    data_from_airtable = await getAirtableData(call.data)
    text = await getListNotes(data_from_airtable, call.data, call)
    await call.message.edit_text(text, reply_markup=rs.notes_kb)

@dp.callback_query_handler(text="first")
async def getFirstNotesFiles(call: CallbackQuery):
    await call.message.answer_document(InputFile.from_url(await getLinkDocumentFromNotes(call)), caption="Вот твой документ")
    await call.message.answer(await getListNotes(
        table_state[call.from_user.id]['table_data'],
        table_state[call.from_user.id]['table_name'], call), reply_markup=rs.notes_kb)
    await call.message.delete()

@dp.callback_query_handler(text="second")
async def getSecondNotesFiles(call: CallbackQuery):
    await call.message.answer_document(InputFile.from_url(await getLinkDocumentFromNotes(call)), caption="Вот твой документ")
    await call.message.answer(await getListNotes(
        table_state[call.from_user.id]['table_data'],
        table_state[call.from_user.id]['table_name'], call), reply_markup=rs.notes_kb)
    await call.message.delete()

@dp.callback_query_handler(text="third")
async def getThirdNotesFiles(call: CallbackQuery):
    await call.message.answer_document(InputFile.from_url(await getLinkDocumentFromNotes(call)), caption="Вот твой документ")
    await call.message.answer(await getListNotes(
        table_state[call.from_user.id]['table_data'],
        table_state[call.from_user.id]['table_name'], call), reply_markup=rs.notes_kb)
    await call.message.delete()

@dp.callback_query_handler(text="prev")
async def getPreviousNotesLists(call: CallbackQuery):
    text = await getPreviousListNotes(call)
    await call.message.edit_text(text, reply_markup=rs.notes_kb)

@dp.callback_query_handler(text="next")
async def getNextNotesLists(call: CallbackQuery):
    text = await getNextListNotes(call)
    await call.message.edit_text(text, reply_markup=rs.notes_kb)

@dp.callback_query_handler(text="back_to_table_list")
async def getNextNotesLists(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_text("Выбери таблицу", reply_markup=rs.notes_menu_kb)
