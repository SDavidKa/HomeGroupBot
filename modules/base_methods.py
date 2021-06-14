from app import airtable_api_key, airtable_base_id
from aiogram.types import Message, CallbackQuery
from asgiref.sync import sync_to_async
import airtable

# Метод получения данных с AirTable
async def getAirtableData(table_name: str):
    table = await sync_to_async(airtable.Airtable)(airtable_base_id, table_name, airtable_api_key)
    return table.get_all()

# Логи
async def getUserLogsFromCallbackQuery(call: CallbackQuery):
    text = f"User: {call.from_user.first_name} {call.from_user.last_name} | {call.from_user.username}" \
           f"\nText: {call.data}" \
           f"\nDate: {call.message.date}\n"
    return text

# Логи
async def getUserLogsFromMessage(message: Message):
    text = f"User: {message.from_user.first_name} {message.from_user.last_name} | {message.from_user.username}" \
           f"\nText: {message.text}" \
           f"\nDate: {message.date}\n"
    return text