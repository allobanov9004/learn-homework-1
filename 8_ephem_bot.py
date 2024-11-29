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
import logging

import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


# PROXY = {
#     'proxy_url': 'socks5://t1.learn.python.ru:1080',
#     'urllib3_proxy_kwargs': {
#         'username': 'learn',
#         'password': 'python'
#     }
# }


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def define_constellation(update, context):
    planet = update.message.text.split()[1].lower()
    today = datetime.today().strftime('%Y/%m/%d')
    if planet == 'mars' or planet == 'марс':
        mars = ephem.Mars()
        mars.compute(today)
        const = f'Mars in {list(ephem.constellation(mars))[1]}'
        update.message.reply_text(const)
    elif planet == 'venus' or planet == 'венера':
        venus = ephem.Venus()
        venus.compute(today)
        const = f'Venus in {list(ephem.constellation(venus))[1]}'
        update.message.reply_text(const)
    elif planet == 'mercury' or planet == 'меркурий':
        mercury = ephem.Mercury()
        mercury.compute(today)
        const = f'Mercury in {list(ephem.constellation(mercury))[1]}'
        update.message.reply_text(const)
    elif planet == 'jupiter' or planet == 'юпитер':
        jupiter = ephem.Jupiter()
        jupiter.compute(today)
        const = f'Jupiter in {list(ephem.constellation(jupiter))[1]}'
        update.message.reply_text(const)
    elif planet == 'saturn' or planet == 'сатурн':
        saturn = ephem.Saturn()
        saturn.compute(today)
        const = f'Saturn in {list(ephem.constellation(saturn))[1]}'
        update.message.reply_text(const)
    elif planet == 'neptune' or planet == 'нептун':
        neptune = ephem.Neptune()
        neptune.compute(today)
        const = f'Neptune in {list(ephem.constellation(neptune))[1]}'
        update.message.reply_text(const)
    elif planet == 'pluto' or planet == 'плутон':
        pluto = ephem.Pluto()
        pluto.compute(today)
        const = f'Pluto in {list(ephem.constellation(pluto))[1]}'
        update.message.reply_text(const)
    elif planet == 'uranus' or planet == 'уран':
        uranus = ephem.Uranus()
        uranus.compute(today)
        const = f'Uranus in {list(ephem.constellation(uranus))[1]}'
        update.message.reply_text(const)   
    else:
        text = 'введите другую планету'
        update.message.reply_text(text)

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def main():
    mybot = Updater("7792134127:AAHuARS3S453V98XTVRYkHGbve7cZd6B8tk", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", define_constellation)) 
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
