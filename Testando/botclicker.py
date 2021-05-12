import telepot
bot = telepot.bot('Token')
bot.getUpdates()
bot.sendMessage(999999999, 'Link')


##CRIANDO UM FUNÇÃO QUANDO RECEBER UMA MENSAGEM

def mensageDelivery(m):
    print(m['text'])
bot.message_loop(mensageDelivery)
if bot.message_loop == True:
    bot.sendMessage(999999999, 'Link')
while True:
    pass

