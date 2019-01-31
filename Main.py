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
from funcoes import funcoes
import os


bot = meuBot() # Classe bot
calculo = operacoes_matematica() # Classe Trata com Calculos
tools = Ferramentas()
myvoice = voz()
ver_data = funcoes()
#funcao que verifica a entrada do usuario e outra variavel de comparacao




def meuInput(entrada, entrada_ver):
    if(entrada == entrada_ver):
        return 0
    else:
        return 1



myvoice.fala('Me fale o seu nome: ')
nome = input('Me fale o seu nome: ')
myvoice.fala('Olá %s' %str(nome))

if(tools.horas() > 4 and tools.horas() < 12 ):
    print('Bot >> Bom Dia, %s' %str(nome))
    myvoice.fala('Bom Dia %s' %str(nome))
        
elif(tools.horas() > 11 and tools.horas() < 18 ):
    print('Bot >> Boa Tarde %s' %str(nome))
    myvoice.fala('Boa Tarde %s' %str(nome))
        
elif(tools.horas() > 17 and tools.horas() < 5 ):
    print('Bot >> Boa Noite %s' %str(nome))
    myvoice.fala('Boa Noite %s' %str(nome))



    
while True:


    
    #pega a pergunta        
    entrada = input('You >> ')
    #verifica a resposta do Bot
    
    saida = bot.verifica(entrada)
    
    print("\n")

    #pergunta - mais complexas

   
    if(meuInput(entrada, "sair") == 0 or meuInput(entrada, "xau") == 0 or meuInput(entrada, "adeus") == 0):
        myvoice.fala('Saindo cara')
        print("Bot >> Saindo cara....")
        exit(1)
    elif(meuInput(entrada, "abrir terminal de comandos") == 0 ):
        tools.executar(saida, "cmd")
        myvoice.fala('Abrindo terminal de comandos')
        
    elif(meuInput(entrada, "abrir navegador") == 0 ):
        tools.system(saida)
        myvoice.fala('Abrindo navegador')
        
    elif(meuInput(entrada, "raiz de") == 0):
        myvoice.fala('Digite o valor para x:')
        x = int(input("Bot >> Digite o valor:  "))
        raiz = calculo.raiz(x)
        myvoice.fala("A raiz quadrada de %d é %d" %(x, raiz))
        print("Bot >> A raiz quadrada de %d é %d" %(x, raiz))
        
    elif(meuInput(entrada, "que horas são") == 0 or meuInput(entrada, "me fale as horas") == 0 or meuInput(entrada, "são que horas") == 0):
        horas = tools.horas()
        minutos = tools.minutos()
        myvoice.fala("São %d Horas e %d Minutos " %(horas, minutos))    
        print("Bot >> São %d Horas e %d Minutos " %(horas, minutos))

    elif(meuInput(entrada, "comandos") == 0):
        myvoice.fala("Digite o comando cara: ")
        comando = input("Bot >> Digite o comando cara: ")
        myvoice.fala("Digite os argumentos : ")
        argumentos = input("Bot >> Digite os argumentos: ")
        tools.executar(comando, argumentos)

    else:
        print("Bot >> "+saida)
        myvoice.fala(saida)

    verdade = True
