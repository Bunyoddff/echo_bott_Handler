import telegram
bot=telegram.Bot(token='8877209931:AAH6Bkhk9IfRQ53_00N7Ux3QEfr2p2YXb8M')
update=bot.getUpdates()
for i in 
chat_i=update[-1].message.chat_id
bot.sendMessage(chat_i,update[-1].message.text)