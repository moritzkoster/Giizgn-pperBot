import json
import random
import secrets

from telegram.ext import Updater, MessageHandler, Filters

with open('token.json', 'r') as token_file:
    token_dict = json.load(token_file)

updater = Updater(token=token_dict["token"])
dispatcher = updater.dispatcher


def message_handler(bot, update):
    messageStr = update.message.text.lower().translate({ord(i): None for i in '.:;,?'})
    if messageStr == "wie isst me nutella":
        bot.send_message(chat_id=update.message.chat_id, text="Selbstverständlich ohni Butter, nur Scheusale, Barbare und anderi Ranzlinge essed Nutella mit Butter!!!")
    if messageStr == "wie goot d welt under":
        bot.send_message(chat_id=update.message.chat_id, text="Der uralte Vulkan Kronos reisst beim grossen Glockenschlag auf, und wenn der Ring da nicht pünktlich in die brodelnde Glut geworfen wird, dann wird die ganze Welt mit Fondue überbacken")
    message = update.message.text.lower().split()
    print(message)
    didSend = False
    if "pflumewäldli" in message:
        bot.send_message(chat_id=update.message.chat_id, text="Was für ein schöner Ort!")
        didSend = True
    if "giizig" in message or "gizig" in message:
        bot.send_message(chat_id=update.message.chat_id, text="und wie!")
        didSend = True
    if "livigno" in message:
        bot.send_message(chat_id=update.message.chat_id, text="Was für ein hässlicher Name!")
        didSend = True
    if "gester" in message:
        bot.send_message(chat_id=update.message.chat_id, text="gester?! Da schaffed mer nie!!")
        didSend = True

    if not didSend:
        bot.send_message(chat_id=update.message.chat_id, text="I ha di ned verstande du Stinkdachs")

dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
updater.start_polling()
