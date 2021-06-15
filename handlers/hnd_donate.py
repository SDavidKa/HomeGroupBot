from app import dp, bot, payments_provider_token
from modules import getUserLogsFromMessage
from keyboards import kb_menu
from aiogram.types import Message

# Глобальная переменная
previous_message_text = dict()

# Пункт "Слово жизни"
@dp.message_handler(text='Слово жизни')
async def getDonate_WordOfLife(message: Message):
    await saveLastMessage(message, 'donate')
    await message.answer("Мы все больше используем электронные платежи в повседневной жизни. "
                         "Так и церковь идет в ногу со временем."
                         "\nЭта форма даяний создана для того, чтобы Вы могли осуществлять регулярные "
                         "финансовые пожертвования через интернет."
                         "\n\nВведи сумму пожертвования:")
    print(await getUserLogsFromMessage(message))

# Пункт "Строим церковь"
@dp.message_handler(text='Строим церковь')
async def getDonate_BuildChurch(message: Message):
    await saveLastMessage(message, 'donate')
    await message.answer("Мы купили второе здание и сейчас нам предстоит совершить"
                         "следующий шаг - перестроить его и сделать ремонт, чтобы мы смогли"
                         "использовать его в качестве молодеждного центра."
                         "\n\nВведи сумму пожертвования:")
    print(await getUserLogsFromMessage(message))

# Пункт "Израиль"
@dp.message_handler(text='Израиль')
async def getDonate_Israel(message: Message):
    await saveLastMessage(message, 'donate')
    await message.answer("Мы помогаем евреям вернуться на их родину. "
                         "Участвуем в строительстве мемориалов и памятников жертв Холокоста. "
                         "Помогаем бывшим узникам концентрационных лагерей и гетто, снабжая их необходимыми "
                         "лекарствами и оказывая другую благотворительную помощь."
                         "Мы принимаем активное участие в развитии Иудео-Христианского Диалога "
                         "и проводим совместные молитвы за Израиль."
                         "\n\nВведи сумму пожертвования:")
    print(await getUserLogsFromMessage(message))

# Пункт "Социальная работа"
@dp.message_handler(text='Социальная работа')
async def getDonate_WordOfLife(message: Message):
    await saveLastMessage(message, 'donate')
    await message.answer("Помощь ближнему — наша ответственность и возможность проявить любовь Бога здесь, на земле. "
                         "Иисус шел туда, где нуждающихся было много, а готовых помочь — не отвернуться — в разы меньше."
                         "\nМы как церковь можем поступать так же: протягивать руки, поддерживать, обнимать, кормить, "
                         "благословлять, не отворачиваться, не игнорировать."
                         "\n\nВведи сумму пожертвования:")
    print(await getUserLogsFromMessage(message))

# Пункт "Миссия: до края земли"
@dp.message_handler(text='Миссия: до края земли')
async def getDonate_ToEndOfEarth(message: Message):
    await saveLastMessage(message, 'donate')
    await message.answer("Согласно великому поручению Христа, сказанного в Матфея 28:19: "
                         "«Итак, идите, научите все народы, крестя их во имя Отца и Сына и Святого Духа», "
                         "основным видом нашей миссионерской деятельности является обучения христианской вере "
                         "по всему миру, в том числе с помощью организации образовательных программ — от библейских "
                         "школ до высшего богословского образования. Мы отправляем проповедников в церкви России, "
                         "Европы, стран Азии и Ближнего Востока, чтобы они передавали учение веры и взращивали новых "
                         "служителей поместных церквей. Также мы активно участвуем в организации конференций в городах "
                         "России и мира, на которых тысячи людей слышат Евангелие."
                         "\n\nВведи сумму пожертвования:")
    print(await getUserLogsFromMessage(message))

# Пункт "500 по 500"
@dp.message_handler(text='500 по 500')
async def getDonate_500on500(message: Message):
    await saveLastMessage(message, 'donate')
    await message.answer("«500 по 500» — это 500 открытых к даянию сердец, готовых жертвовать 500 рублей "
                         "каждый месяц на служение, которое осуществляет наша команда на миссионерских полях. "
                         "\nЖертвуя 500 рублей каждый месяц, ты становишься частью большой миссионерской команды. "
                         "И вместе мы сможем быть максимально эффективными в наших делах для Бога: поддерживать в вере "
                         "наших братьев и сестер, христиан веры евангельской (пятидесятников), в Таджикистане, "
                         "Сербии и во Вьетнаме и вместе достигать «потерянных» по всему миру.")
    await sendInvoice(message, '500 по 500', 'Спасибо за ваше пожертвование', 'Добровольное пожертвование', 500)
    print(await getUserLogsFromMessage(message))

# Пункт "Реквизиты"
@dp.message_handler(text='Реквизиты')
async def getDonate_Requisite(message: Message):
    await saveLastMessage(message, 'requisites')
    await message.answer("Местная религиозная организация"
                         "\nБиблийский центр христиан"
                         "\nверы евангельской \"Слово Жизни\""
                         "\nИНН: 7726025431"
                         "\nКПП: 771701001"
                         "\nБанк получателя ПАО СБЕРБАНК"
                         "\nБИК: 044525225"
                         "\nСчет: 40703810838340100391"
                         "\nК/сч: 30101810400000000225")
    print(await getUserLogsFromMessage(message))

# Возвращение к меню
@dp.message_handler(text='Вернуться в меню')
async def getMenu(message: Message):
    await saveLastMessage(message, 'back to menu')
    await message.answer("Выбери необходимый пункт в меню", reply_markup=kb_menu.menu_kb)
    print(await getUserLogsFromMessage(message))

# Обрабатываем сумму пожертваования
@dp.message_handler()
async def getAmountForDonate(message: Message):
    if previous_message_text[message.from_user.id]['action'] == 'donate':
        amount = int(message.text)
        title = previous_message_text[message.from_user.id]['last_message']
        await sendInvoice(message=message, title=title, description='Спасибо за ваше пожертвование',
                          label='Добровольное пожертвование', amount=amount)

async def saveLastMessage(message: Message, action: str):
    global previous_message_text
    previous_message_text.update(user_id=message.from_user.id)
    previous_message_text[message.from_user.id] = {
        'last_message': message.text,
        'action': action
    }

async def sendInvoice(message: Message, title: str, description: str, label: str, amount: int):
    await bot.send_invoice(
        message.from_user.id,
        title=title,
        description=description,
        provider_token=payments_provider_token,
        currency='rub',
        start_parameter='',
        prices=[{
            'label': label,
            'amount': amount*100
        }],
        payload={
            'unique_id': f'{message.from_user.id}{message.date}',
            'provider_token': payments_provider_token
        }
    )
