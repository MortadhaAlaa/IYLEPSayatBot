from telegram.ext import MessageHandler, CommandHandler, Filters, Updater
import os, logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='مرحبا ب بوت السايات الخاص بلايلب..🔥\nاكتب السؤال الي تحب تسألة ، حيوصل للالومناي بصورة مجهولة! \nويتم الرد عليه باقرب وقت بلقناة❤️')

def message(bot, update):
    if update.message.chat_id == '-273378117':
        return
    bot.send_message(chat_id='-273378117', text=update.message.text)
    bot.send_message(chat_id=update.message.chat_id, text='تم ارسال رسالتك بصورة مجهولة،\nانتظر الجواب قريبا على القناة ❤️..')
    bot.forward_message(chat_id='-253860529', from_chat_id=update.message.chat_id, message_id=update.message.message_id)

def error(bot, update, error):
     logging.warning('Update "%s" caused error "%s"' % (update, error))    
u = Updater(os.environ['TELEGRAM_TOKEN'])
d = u.dispatcher
d.add_handler(CommandHandler('start', start))
d.add_handler(MessageHandler(Filters.text, message))
d.add_error_handler(error)

u.start_polling()
u.idle()