from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
chatbot = ChatBot('Alfa')
chat = ['Oi,','Olá','Bom dia ?','Boa noite','Como vai ?','Estou bem', 'Obrigado']
trainer = (ListTrainer)
trainer.train(chat)
while True:
    request = input('text')
    print(bot.get_response(request))