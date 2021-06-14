from app import dp
from modules import getUserLogsFromMessage
from aiogram.types import Message

# Пункт "Пожертвовать"
@dp.message_handler(text='Пожертвовать')
async def getDonate_WordOfLife(message: Message):
    await message.answer("Пожертвовать можно на сайте церкви: https://wolrus.org/donate")
    print(await getUserLogsFromMessage(message))


# Пункт "Реквизиты"
@dp.message_handler(text='Реквизиты')
async def getDonate_Requisite(message: Message):
    await message.answer("Местная религиозная организация" +
                         "\nБиблийский центр христиан" +
                         "\nверы евангельской \"Слово Жизни\"" +
                         "\nИНН: 7726025431" +
                         "\nКПП: 771701001" +
                         "\nБанк получателя ПАО СБЕРБАНК" +
                         "\nБИК: 044525225" +
                         "\nСчет: 40703810838340100391" +
                         "\nК/сч: 30101810400000000225")
    print(await getUserLogsFromMessage(message))
