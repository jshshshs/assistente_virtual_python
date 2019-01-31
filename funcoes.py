##############################################################################################################################################
#
#   ASSISTENTE VIRTUAL - DESENVOLVIDO POR MANOEL VITOR - 
#   
#   FUNCAO PRINCIPAL DO PROGRAMA
#
##############################################################################################################################################

#-*- utf-8 -*-

from meuBot import meuBot
from operacoes_matematica import operacoes_matematica
from Ferramentas import Ferramentas
from voz import voz
from datetime import datetime

hora = datetime.now()
myvoice = voz()

class funcoes():

    def _init_(self):
        pass
    
    def hora_atual(self):
        
        data_atual = datetime.now()
        hora = data_atual.hour

        if(hora >= 5 and  hora < 12):
            try:
                print('Bot >> Bom Dia')
                myvoice.fala('Bom Dia')
            except:
                print('Bot >> Bom Dia')
        elif(hora >= 12 and hora < 18):
            try:
                print('Bot >> Boa Tarde')
                myvoice.fala('Boa Tarde,')
            except:
                print('Bot >> Boa Tarde')
        elif(hora >= 18 and hora < 5):
            try:
                print('Bot >> Boa Noite')
                myvoice.fala('Boa Noite')
            except:
                print('Bot >> Boa Noite')
