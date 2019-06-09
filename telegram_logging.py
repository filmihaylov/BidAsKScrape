import telegram

def send(msg):
    try:
	    bot = telegram.Bot(token="")
	    bot.sendMessage(chat_id="244146002", text=msg)
    except:
        pass
