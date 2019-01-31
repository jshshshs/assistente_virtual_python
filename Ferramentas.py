##############################################################################################################################################
#
#   ASSISTENTE VIRTUAL - DESENVOLVIDO POR MANOEL VITOR - 
#   
#   ALGUMAS FERRAMENTAS DO SISTEMA OPERACIONAL - COMANDOS ETC..
#
##############################################################################################################################################

#-*- utf-8 -*-
from datetime import datetime
import io
import os
import subprocess # executar comandos do windows - MS DOS

# Classe que trabalha com o sistema do, No meu caso Windows 7
# Algoritmo - Manoel Vitor
# Open-Source - Você está livre para utilizar-lo, desde que não esquece
# de reconhecer que eu desenvolvi, pode usar para seus trabalhos.

class Ferramentas():

    def _init_(self):
        pass

    def executar(self, comandos, attributos):
        subprocess.call(comandos+" "+attributos, shell = True)
        
    def system(self, comandos):
        os.system(comandos)
        
    def data(self):
        data_atual = datetime.now()
        suaData = data_atual.today
        return suaData
    def dia(self):
        data_atual = datetime.now()
        dia = data_atual.day
        return dia
    def mes(self):
        data_atual = datetime.now()
        mes = data_atual.month
        return mes

    def ano(self):
        data_atual = datetime.now()
        ano = data_atual.year
        return ano
                
    def horas(self):
        data_atual = datetime.now()
        horas = data_atual.hour
        return horas

    def minutos(self):
        data_atual = datetime.now()
        minutos = data_atual.minute
        return minutos

  
