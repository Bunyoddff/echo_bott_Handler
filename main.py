import telegram
from dotenv import loaddotenv
import os
loaddotenv()
token=os.getenc('token')
bot=telegram.Bot(token)
update=bot.getUpdates()
for i in 
chat_i=update[-1].message.chat_id
bot.sendMessage(chat_i,update[-1].message.text)