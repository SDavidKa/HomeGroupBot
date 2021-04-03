from app import bot, dp, admin_id
from aiogram.types import Message, InputMediaDocument, CallbackQuery
from keyboards import donate, menu, resource, leadershipCourse

async def send_to_admin_start(dp):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")

# Первое приветствие пользователя
@dp.message_handler(commands = ['start'])
async def startsMessage(message: Message):
    await message.answer("Выбери необходимый пункт в меню", reply_markup=menu.menu_kb)

# Возвращение к меню
@dp.message_handler(text = 'Вернуться в меню')
async def getMenu(message: Message):
    await message.answer("Выбери необходимый пункт в меню", reply_markup=menu.menu_kb)

# Переход в раздел "Материалы"
@dp.message_handler(text = 'Материалы')
async def getResources(message: Message):
    await message.answer("Здесь ты найдешь конспекты и другие материалы для домашних групп."
                         "\n\nВыбери раздел:", reply_markup=resource.resource_kb)

# Выдача конспектов воскресной проповеди
@dp.message_handler(text = 'Вс. проповеди')
async def getPreaching(message: Message):
    await message.answer("Тема 1"
                         "\nНазвание конспекта 1")

# Выдача конспектов
@dp.message_handler(text = 'Конспекты')
async def getNotes(message: Message):
    await message.answer("Выбери тему:", reply_markup=resource.notesName_kb)

@dp.callback_query_handler(text='inputFile_1')
async def getFile(call: CallbackQuery):
    doc=InputMediaDocument(resource.ulrsDocument[1])
    await call.message.answer_document(document=[doc])

# Выдача расписания
@dp.message_handler(text = 'Расписание')
async def getSchedule(message: Message):
    await message.answer("Расписание ближайших мероприятий церкви в Москве")

# Выдача материалов лидерского курса
@dp.message_handler(text = 'Лидерские курсы')
async def getLeadershipCourse(message: Message):
    await message.answer("Здесь ты найдешь материалы для лидеров домашних групп:", reply_markup=leadershipCourse.leadershipCourse_kb)

# Переход в раздел "Пожертвование"
@dp.message_handler(text = 'Пожертвовать')
async def getDonate(message: Message):
    await message.answer("Благодаря твоей поддержке мы можем" +
    "\nпродолжать насаждать церкви и распространять Евангелие!" +
    "\n\nВыбери, на то что ты пожертвуешь:", reply_markup=donate.donate_kb)

# Пункт "Строим церковь"
@dp.message_handler(text = 'Строим церковь')
async def getDonate_BuildChurch(message: Message):
    await message.answer("Мы купили второе здание и сейчас нам предстоит совершить" +
    "\nследующий шаг - перестроить его и сделать ремонт, чтобы мы смогли" +
    "\nиспользовать его в качестве молодеждного центра." +
    "\n\nВведи сумму пожертвования:")

# Пункт "Израиль"
@dp.message_handler(text ='Израиль')
async def getDonate_Israel(message: Message):
    await message.answer("Пока пользуйся этим сайтом: https://wolrus.org/donate")

# Пункт "До края земли"
@dp.message_handler(text ='До края земли')
async def getDonate_ToEndOfEarth(message: Message):
    await message.answer("Пока пользуйся этим сайтом: https://wolrus.org/donate")

# Пункт "500 по 500"
@dp.message_handler(text ='500 по 500')
async def getDonate_500on500(message: Message):
    await message.answer("Пока пользуйся этим сайтом: https://wolrus.org/donate")

# Пункт "Слово жизни"
@dp.message_handler(text ='Слово жизни')
async def getDonate_WordOfLife(message: Message):
    await message.answer("Пока пользуйся этим сайтом: https://wolrus.org/donate")

# Пункт "Реквизиты"
@dp.message_handler(text ='Реквизиты')
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

# Неизвестная команда
@dp.message_handler()
async def unknownCommands(message: Message):
    await message.reply("Незнаю такой команды. Выбери что-то из меню")
