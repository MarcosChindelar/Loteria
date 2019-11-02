# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 09:49:58 2019

@author: Marcos Chindelar
"""

from random import randint
import webbrowser
#Questão 1#
class Loteria:
    __dezenas = None
    __resultado = None
    __total_jogos = None
    __jogos = None
#Questão 2#
    def getDezenas(self):
        return self.__dezenas
    def getResultado(self):
        return self.__resultado
    def getTotalJogos(self):
        return self.__total_jogos
    def getJogos(self):
        return self.__jogos
    def setDezenas(self,dezenas):
        self.__dezenas = dezenas
    def setResultado(self,resultado):
        self.__resultado = resultado
    def setTotalJogos(self,total):
        self.__total_jogos = total
    def setJogos(self,jogos):
        self.__jogos = jogos
#Questão 3#
    def __init__(self,dezenas,total):
        if dezenas<6 or dezenas>10 or type(dezenas)!=int or type(total)!=int:
            print("Valor inválido.")
            return
        else:
            self.setDezenas(dezenas)
            self.setTotalJogos(total)
#Questão 4#
    def _resultado(self):
        resultado = []
        while len(resultado)<self.getDezenas():
            dezena = randint(0,60)
            if dezena in resultado:
                dezena = randint(0,60)
            else:
                resultado.append(dezena)
        resultado.sort()
        return resultado
#Questão 5#
    def realizaJogos(self):
        self.__jogos = []
        for i in range(self.getTotalJogos()):
             self.__jogos.append(self._resultado())
#Questão 6#
    def sorteio(self):
        resultado = []
        while len(resultado) < self.getDezenas():
            dezena = randint(0,60)
            if dezena in resultado:
                dezena = randint(0,60)
            else:
                resultado.append(dezena)
            resultado.sort()
            self.setResultado(resultado)
#Questão 7#
    def confere(self):
        acertos = []
        for i in range(self.getTotalJogos()):
            n = 0
            for j in range(self.getDezenas()):
                if self.__resultado[j] in self.__jogos[i]:
                    n = n+1
            acertos.append(n)
        tabela = ""
        tabela = tabela + "<html><head><title>Resultados dos Sorteios</title></head><body>"
        tabela = tabela + "<table border = 1>"
        tabela = tabela + "<tr><td align='center'>Sorteio</td><td align='center'>Acertos</td></tr>"
        for i in range(self.getTotalJogos()):
            tabela = tabela + "<tr>"
            tabela = tabela + "<td align='center'>" + str(self.__jogos[i]) + "</td>"
            tabela = tabela + "<td align='center'>" + str(acertos[i]) + "</td>"
            tabela = tabela + "</tr>"
        tabela = tabela + "</table></body></html>"
        self.criaPagina(tabela)
        return tabela
#Método para criar uma página html e exibi-la contendo os resultados do sorteio e o número de acertos#    
    def criaPagina(self,tabela):
        with open("Loteria.html",'w') as f:
            print(tabela,file=f)
            f.close()
        webbrowser.open("Loteria.html",new=2,autoraise=True)

        
        