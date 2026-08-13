from telegram.ext import Updater, MessageHandler, Filters
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('token')


updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher

def salom(update, context):
    update.message.reply_text('Hello! How can I help you today')
def other(update, context):
    update.message.reply_text(update.message.text)

def bye(update,context):
    update.message.reply_text('Goodbye! Have great day!')

hello_handler = MessageHandler(Filters.regex('hello'), salom)
other_handler = MessageHandler(Filters.text & ~Filters.regex('hello'),other)
bye_handler = MessageHandler(Filters.regex('bye'), bye)
dispatcher.add_handler(hello_handler)
dispatcher.add_handler(bye_handler)
dispatcher.add_handler(other_handler)

print("i am here now...")
updater.start_polling()
updater.idle()