from telegram.ext import Updater, CommandHandler,MessageHandler, Filters
import logging
import settings
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = ('Вызван/start')
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first.name, update.message.text) 
    logging.info("User: %s, Chat id: %s, Message: %s",update.message.chat.username, update.message.chat.id, 
    update.message.text)
    update.message.reply_text(user_text)

def planet_canstellation(bot,update):
    date = datetime.date(now).strftime('%Y/%m/%d')
    user_text = update.message.text.split()
    planet = ephem.user_text(date)
    if user_text == 'Марс'
        print(ephem.constellation(Марс))
    elif user_text == 'Венера'
        print(ephem.constellation(Венера))
    elif user_text == 'Меркурий'
        print(ephem.constellation(Меркурий))
    elif user_text == 'Юпитер'
        print(ephem.constellation(Юпитер))
    elif user_text == 'Земля'
        print(ephem.constellation(Земля))
    elif user_text == 'Плутон'
        print(ephem.constellation(Плутон))
    elif user_text == 'Уран'
        print(ephem.constellation(Уран))
    elif user_text == 'Сатурн'
        print(ephem.constellation(Сатурн))
    elif user_text == 'Земля'
        print(ephem.constellation(Земля))
def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    print(1)
    logging.info('Бот запускается')
    dp = mybot.dispatcher
    print(2)
    dp.add_handler(CommandHandler('start', greet_user))
    print(3)
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    print(4)
    mybot.idle()

main()