from app import dp
from keyboards import kb_resource as rs
from modules import getAirtableData, getUserLogsFromCallbackQuery
from aiogram.types import InputFile, CallbackQuery

# Глобальная переменная
table_state = dict()

@dp.callback_query_handler(text="Главные документы")
async def getNotesFromTableMainDocs(call: CallbackQuery):
    data_from_airtable = await getAirtableData(call.data, 'Name')
    text = await getListNotes(data_from_airtable, call.data, call)
    markup = rs.notes_kb(table_state[call.from_user.id]['table_count'], len(table_state[call.from_user.id]['list_name']))
    await call.message.edit_text(text, reply_markup=markup)
    print(await getUserLogsFromCallbackQuery(call))

@dp.callback_query_handler(text="Гостеприимство")
async def getNotesFromTableMainDocs(call: CallbackQuery):
    data_from_airtable = await getAirtableData(call.data, 'Name')
    text = await getListNotes(data_from_airtable, call.data, call)
    markup = rs.notes_kb(table_state[call.from_user.id]['table_count'], len(table_state[call.from_user.id]['list_name']))
    await call.message.edit_text(text, reply_markup=markup)
    print(await getUserLogsFromCallbackQuery(call))

@dp.callback_query_handler(text="Конспекты с ДГ")
async def getNotesFromTableMainDocs(call: CallbackQuery):
    data_from_airtable = await getAirtableData(call.data, 'Name')
    text = await getListNotes(data_from_airtable, call.data, call)
    markup = rs.notes_kb(table_state[call.from_user.id]['table_count'], len(table_state[call.from_user.id]['list_name']))
    await call.message.edit_text(text, reply_markup=markup)
    print(await getUserLogsFromCallbackQuery(call))

@dp.callback_query_handler(text="Книги для обязательного прочтения")
async def getNotesFromTableMainDocs(call: CallbackQuery):
    data_from_airtable = await getAirtableData(call.data, 'Name')
    text = await getListNotes(data_from_airtable, call.data, call)
    markup = rs.notes_kb(table_state[call.from_user.id]['table_count'], len(table_state[call.from_user.id]['list_name']))
    await call.message.edit_text(text, reply_markup=markup)
    print(await getUserLogsFromCallbackQuery(call))

@dp.callback_query_handler(text="обучающие аудио для лидеров")
async def getNotesFromTableMainDocs(call: CallbackQuery):
    data_from_airtable = await getAirtableData(call.data, 'Name')
    text = await getListNotes(data_from_airtable, call.data, call)
    markup = rs.notes_kb(table_state[call.from_user.id]['table_count'], len(table_state[call.from_user.id]['list_name']))
    await call.message.edit_text(text, reply_markup=markup)
    print(await getUserLogsFromCallbackQuery(call))

@dp.callback_query_handler(text="конспекты для окружных лидеров")
async def getNotesFromTableMainDocs(call: CallbackQuery):
    data_from_airtable = await getAirtableData(call.data, 'Name')
    text = await getListNotes(data_from_airtable, call.data, call)
    markup = rs.notes_kb(table_state[call.from_user.id]['table_count'], len(table_state[call.from_user.id]['list_name']))
    await call.message.edit_text(text, reply_markup=markup)
    print(await getUserLogsFromCallbackQuery(call))

@dp.callback_query_handler(text=rs.list_handlers_docs)
async def getFileFromNote(call: CallbackQuery):
    await call.message.answer_document(InputFile.from_url(
        url=await getLinkDocumentFromNotes(call)),
        caption=await getNameOfDocument(call))
    markup = rs.notes_kb(table_state[call.from_user.id]['table_count'], len(table_state[call.from_user.id]['list_name']))
    await call.message.answer(await getListNotes(
        table_state[call.from_user.id]['table_data'],
        table_state[call.from_user.id]['table_name'], call), reply_markup=markup)
    await call.message.delete()
    print(await getUserLogsFromCallbackQuery(call))

@dp.callback_query_handler(text="prev")
async def getPreviousNotesLists(call: CallbackQuery):
    text = await getPreviousListNotes(call)
    markup = rs.notes_kb(table_state[call.from_user.id]['table_count'], len(table_state[call.from_user.id]['list_name']))
    await call.message.edit_text(text, reply_markup=markup)
    print(await getUserLogsFromCallbackQuery(call))

@dp.callback_query_handler(text="next")
async def getNextNotesLists(call: CallbackQuery):
    text = await getNextListNotes(call)
    markup = rs.notes_kb(table_state[call.from_user.id]['table_count'], len(table_state[call.from_user.id]['list_name']))
    await call.message.edit_text(text, reply_markup=markup)
    print(await getUserLogsFromCallbackQuery(call))

@dp.callback_query_handler(text="back_to_table_list")
async def getTableList(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_text("Выбери таблицу", reply_markup=rs.notes_menu_kb)
    print(await getUserLogsFromCallbackQuery(call))

# Метод вывода списка тем
async def getListNotes(data: dict, table_name: str, call: CallbackQuery):
    global table_state
    answer = f"Выбери тему таблицы «{table_name}»:"
    text = ""
    counter = 0
    names = list()
    for note in data:
        names.append(note['fields']['Name'])

    if len(names) >= (counter + 10) > 0:
        stop = counter + 10

        while counter < stop:
            text += f"\n{counter + 1}) {names[counter]}"
            counter += 1

    else:
        while counter < len(names):
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

    if len(names) >= (counter + 10) > 0:
        stop = counter + 10

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
    if counter > 10 and (counter % 10) != 0:
        counter = (counter - (counter % 10)) - 10
    elif 10 <= counter <= 20:
        counter = 0
    else:
        counter -= 20

    if (counter + 10) > 0:
        stop = counter + 10

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

# Метод вывода выбранного наименования документа
async def getNameOfDocument(call: CallbackQuery):
    name = ""
    message = call.message.text
    number = call.data.split("doc_")[1]
    names = message.split("\n")
    names.pop(0)
    for n in names:
        if not (n.find(f"{number})")):
            new_name = n.split(f"{number}) ")
            new_name.pop(0)
            name = new_name[0]
    return name

# Метод вывода ссылки на документ
async def getLinkDocumentFromNotes(call: CallbackQuery):
    global table_state
    data = await getAirtableData(table_state[call.from_user.id]['table_name'], 'Name')
    link = ""
    name = await getNameOfDocument(call)

    for note in data:
        if note['fields']['Name'] == name:
            link = note['fields']['Attachments'][0]['url']
    return link
