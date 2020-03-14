import json
import random

from telegram.ext import Updater, MessageHandler, Filters

with open('token.json', 'r') as token_file:
    token_dict = json.load(token_file)


updater = Updater(token=token_dict["token"])
dispatcher = updater.dispatcher



def message_handler(bot, update):
    message = update.message.text.lower().split()



dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
updater.start_polling()
