from telegram.ext import Updater, MessageHandler, Filters
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('token')
hoto_counter=0

updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher

def salom(update, context):
    update.message.reply_text('Hello! How can I help you today')
def other(update, context):
    update.message.reply_text(update.message.text)

def bye(update,context):
    update.message.reply_text('Goodbye! Have great day!')
def photo_count(update,context):
    if 'counter' not in context.user_data:
        context.user_data['counter']=0
    photo_id=update.message.photo[-1].file_id
    if update.message.photo:
        context.user_data['counter']+=1
        total=context.user_data['counter']
    update.message.reply_photo(
        photo=photo_id,
        caption=f'Photo received! Total photos: {total}'
    )
def sticker_count(update, context):
    if 'stiker_counter' not in context.user_data:
        context.user_data['stiker_counter']=0
    sticker_id=update.message.sticker.file_id
    if update.message.sticker:
        context.user_data['stiker_counter']+=1
        totall=context.user_data['stiker_counter']
    update.message.reply_sticker(
        sticker=sticker_id)
    update.message.reply_text(f'Nice sticker! Total stickers: {totall}')
hello_handler = MessageHandler(Filters.regex('hello'), salom)
other_handler = MessageHandler(Filters.text & ~Filters.regex('hello'),other)
stats_handler = 0
bye_handler = MessageHandler(Filters.regex('bye'), bye)
photo_handler=MessageHandler(Filters.photo,photo_count)
stiker_handler=MessageHandler(Filters.sticker,sticker_count)
dispatcher.add_handler(hello_handler)
dispatcher.add_handler(bye_handler)
dispatcher.add_handler(other_handler)
dispatcher.add_handler(photo_handler)
dispatcher.add_handler(stiker_handler)

print("i am here now...")
updater.start_polling()
updater.idle()