import asyncio
import os

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery
from dotenv import load_dotenv

load_dotenv()
loop = asyncio.get_event_loop()
bot = Bot(os.getenv("BOT_TOKEN"), parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)
admin_id = os.getenv("ADMIN_ID")
airtable_base_id = os.getenv("AIRTABLE_BASE_ID")
airtable_api_key = os.getenv("AIRTABLE_API_KEY")

if __name__ == "__main__":
    from handlers import dp, send_to_admin_start
    executor.start_polling(dp, on_startup=send_to_admin_start)

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