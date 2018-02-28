#!/usr/bin/env python

from __future__ import print_function

class Lenguaje :
    def __init__(self, caracteres):
        self.caracteres = caracteres

    def getCaracteres(self):
        print ('{', end='')
        for caracter in self.caracteres:      
            if caracter != self.caracteres[-1]:
                print(caracter, end=", ")      
            else:
                print (caracter, end="")

        print ('}')

    def invertir(self):
        newList = []
        for caracter in self.caracteres:
            newList.append(caracter[::-1])

        self.caracteres = newList



