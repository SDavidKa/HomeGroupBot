from app import dp, getUserLogsFromMessage
from aiogram.types import Message


# Пункт "Строим церковь"
@dp.message_handler(text='Строим церковь')
async def getDonate_BuildChurch(message: Message):
    await message.answer("Мы купили второе здание и сейчас нам предстоит совершить" +
                         "\nследующий шаг - перестроить его и сделать ремонт, чтобы мы смогли" +
                         "\nиспользовать его в качестве молодеждного центра." +
                         "\n\nВведи сумму пожертвования:")
    print(await getUserLogsFromMessage(message))


# Пункт "Израиль"
@dp.message_handler(text='Израиль')
async def getDonate_Israel(message: Message):
    await message.answer("Пока пользуйся этим сайтом: https://wolrus.org/donate")
    print(await getUserLogsFromMessage(message))


# Пункт "До края земли"
@dp.message_handler(text='До края земли')
async def getDonate_ToEndOfEarth(message: Message):
    await message.answer("Пока пользуйся этим сайтом: https://wolrus.org/donate")
    print(await getUserLogsFromMessage(message))


# Пункт "500 по 500"
@dp.message_handler(text='500 по 500')
async def getDonate_500on500(message: Message):
    await message.answer("Пока пользуйся этим сайтом: https://wolrus.org/donate")
    print(await getUserLogsFromMessage(message))


# Пункт "Слово жизни"
@dp.message_handler(text='Слово жизни')
async def getDonate_WordOfLife(message: Message):
    await message.answer("Пока пользуйся этим сайтом: https://wolrus.org/donate")
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
