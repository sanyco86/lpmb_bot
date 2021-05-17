"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""

import ephem
import logging
import settings

from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename='log/bot.log', level=logging.INFO)


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Здравствуй, пользователь!')


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def get_constellation(update, context):
    text = update.message.text
    print(text)

    try:
        planet_name = text.split(" ")[1]
        planet = getattr(ephem, planet_name)(date.today())
        constellation = ephem.constellation(planet)
    except AttributeError:
        constellation = 'Планета еще не открыта'

    update.message.reply_text(constellation)


def main():
    my_bot = Updater(settings.TELEGRAM_BOT_TOKEN, use_context=True)
    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', get_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')
    my_bot.start_polling()
    my_bot.idle()

if __name__ == "__main__":
    main()
