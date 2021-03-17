from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

buttonResource = KeyboardButton('Конспекты')
buttonSchedule = KeyboardButton('Расписание')
buttonLeadershipCourse = KeyboardButton('Лидерские курсы')
buttonDonate = KeyboardButton('Пожертвовать')

resource_kb = ReplyKeyboardMarkup(resize_keyboard=True)
resource_kb.row(buttonResource, buttonSchedule)
resource_kb.add(buttonLeadershipCourse)
resource_kb.add(buttonDonate)