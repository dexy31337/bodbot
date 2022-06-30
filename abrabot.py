import os
from bot.bot import Bot
from bot.handler import MessageHandler

CHATID = os.environ["CHATID"]
API_URL_BASE = os.environ["API_URL_BASE"]
TOKEN = os.environ["TOKEN"]

bot = Bot(token=TOKEN, api_url_base=API_URL_BASE)

def message_cb(bot, event):
    print(event)
    if event.data['chat']['type'] == "private" and not event.text.startswith('/'): 
        bot.send_text(chat_id=event.from_chat, text=event.data['from']['firstName']+", Ваше обращение принято и передано в дежурную группу БОД. Мы уже спешим на помошь!")
        msgtext = "Cообщение от @[" + event.data['from']['userId'] + "]\n\n" + event.text
        bot.send_text(chat_id=CHATID, text=msgtext)

bot.dispatcher.add_handler(MessageHandler(callback=message_cb))
bot.start_polling()
bot.idle()
