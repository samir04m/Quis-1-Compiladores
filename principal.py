#!/usr/bin/env python
import lenguaje

entrada = raw_input("Ingrese los caracteres de su lenguaje : ")

entrada = entrada.replace('{', '')
entrada = entrada.replace('}', '')
caracteres = entrada.split(',')

language = lenguaje.Lenguaje(caracteres)
language.invertir()

language.getCaracteres()
