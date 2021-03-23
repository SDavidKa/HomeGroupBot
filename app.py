import asyncio
import os

from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv

load_dotenv()
loop = asyncio.get_event_loop()
bot = Bot(os.getenv("BOT_TOKEN"), parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)
admin_id = os.getenv("ADMIN_ID")

async def on_shutdown(dp):
    await bot.close()

if __name__ == "__main__":
    from handlers.handlers import dp, send_to_admin_start
    executor.start_polling(dp, on_startup=send_to_admin_start, on_shutdown=on_shutdown)
