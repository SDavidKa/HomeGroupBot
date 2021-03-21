from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Объявление кнопок для "Меню"
buttonResource = KeyboardButton('Материалы')
buttonSchedule = KeyboardButton('Расписание')
buttonLeadershipCourse = KeyboardButton('Лидерские курсы')
buttonDonate = KeyboardButton('Пожертвовать')
# Объявление кнопок для "Материалов"
buttonNotes = KeyboardButton('Конспекты')
buttonPreaching = KeyboardButton('Вс. проповеди')
buttonBack = KeyboardButton('Вернуться в меню')
# Объявление кнопок для "Пожертовования"
buttonBuildChurch = KeyboardButton('Строим церковь')
buttonIsrael = KeyboardButton('Израиль')
button500on500 = KeyboardButton('500 по 500')
buttonWordOfLife = KeyboardButton('Слово жизни')
buttonRequisite = KeyboardButton('Реквизиты')
buttonToEndOfEarth = KeyboardButton('До края земли')

# Группировка кнопок для меню
menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
menu_kb.row(buttonResource, buttonSchedule)
menu_kb.add(buttonLeadershipCourse)
menu_kb.add(buttonDonate)

# Группировка кнопок для материалов
resource_kb = ReplyKeyboardMarkup(resize_keyboard=True)
resource_kb.row(buttonNotes, buttonPreaching)
resource_kb.add(buttonBack)

# Группировка кнопок для материалов
donate_kb = ReplyKeyboardMarkup(resize_keyboard=True)
donate_kb.row(buttonBuildChurch, buttonIsrael)
donate_kb.row(buttonToEndOfEarth, button500on500)
donate_kb.row(buttonWordOfLife, buttonRequisite)
donate_kb.add(buttonBack)

#Inline кнопки
buttonSite = InlineKeyboardButton('Перейти на сайт')
webSite_kb = InlineKeyboardMarkup()