###########################################################################################################################
#                                                                                                                         #
#                                                                                                                         #
#                 CHATTEBOT - DEVELOPMENT BY MANOEL VITOR                                                                                                        #
#                                                                                                                         #
###########################################################################################################################

import io
import os
from palavra import palavra

class meuBot():
    
    
    def _init_(self):
        pass
    
    def verifica(self, entrada):

        word = palavra() #biblioteca palavra
        entrada = word.normalizar(entrada)
        resp = "Não conseguir entender sua frase!"
        
        texto_entrada = open("./data/entrada.txt", "r")
        pergunta = texto_entrada.readlines()
        texto_entrada.close()

        texto_saida = open("./data/saida.txt", "r")
        resposta = texto_saida.readlines()
        texto_saida.close()
        

        cont  = 0
        
        for asked in pergunta:
    
            if(entrada+"\n" == asked):
                resp = resposta[cont]
                return resp
            cont +=1
            
        return resp
