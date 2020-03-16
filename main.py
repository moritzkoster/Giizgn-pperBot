import json
import random

from telegram.ext import Updater, MessageHandler, Filters

with open('token.json', 'r') as token_file:
    token_dict = json.load(token_file)

updater = Updater(token=token_dict["token"])
dispatcher = updater.dispatcher


def message_handler(bot, update):
    messageStr = update.message.text.lower().translate({ord(i): None for i in '.:;,?'})
    if messageStr == "wie isst me nutella":
        bot.send_message(chat_id=update.message.chat_id, text="Selbstverständlich ohni Butter, nur Scheusale, Barbare und anderi Ranzlinge essed Nutella mit Butter!!!")
    message = update.message.text.lower().split()
    print(message)
    if "pflumewäldli" in message:
        bot.send_message(chat_id=update.message.chat_id, text="Was für ein schöner Ort!")
    if "giizig" in message:
        bot.send_message(chat_id=update.message.chat_id, text="und wie!")



dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
updater.start_polling()
