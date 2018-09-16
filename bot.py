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