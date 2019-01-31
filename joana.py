##############################################################################################################################################
#
#   ASSISTENTE VIRTUAL - DESENVOLVIDO POR MANOEL VITOR - 
#   
#   Prototipo usando pura inteligencia artficial
#
##############################################################################################################################################

#-*- utf-8 -*-

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from voz import voz



myBot = ChatBot('Joana')
myVoice = voz()

myBot.set_trainer(ListTrainer)



arquivos1 = open("./data/dados1.txt", "r")
linhas1 = arquivos1.readlines()


myBot.train(linhas1)


arquivos1.close()

while(True):

    perguntar = input('You >>  ')
    responder = myBot.get_response(perguntar)
    print('Bot >> %s' %str(responder))
    myVoice.fala(responder)

