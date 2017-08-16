#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# xolo/__init__.py
# Standard library for asquel interpreter
# Analizer and strings
#
# This is part of the Asquel project.
# (c)2017 Alan Ramirez Zatarain
# https://github.com/SoyZatarain/asquel
#


import os
import sys
import platform
import operator

def limpiar():
    if os.name == "posix":  #Diferenciar entre sistemas
        os.system ("clear") #Todos los posix aceptan el mismo comando para esto
    else:
        os.system ("cls")   #Windows acepta este comando

def derechos():
    if os.name == "posix":
        sys.stdout.write("\x1b]2;Asquel 0.1 para %s\x07" % platform.system())  #Aqui se diferencia entre los posix (OS X, Linux, BSD, etc.)
        print(chr(27)+"[1;33m"+'Copyright (c)2017 Alan Ramirez Zatarain')            #Copyrights
        print('http://asquel.hol.es/LICENSE\n'+chr(27)+"[0;37m")    #Solo actualizaciones, no cambios de licencia
    else:
        os.system ("title Asquel 0.1 para Windows")
        print('Copyright (c)2017 Alan Ramirez Zatarain')
        print('http://asquel.hol.es/LICENSE\n')

class TipoDeSimbolo:
	numero, suma, resta, multiplicacion, division, final = "num", "suma", "resta", "multiplicacion", "division", "final"
	operadores = { '+': suma, '-': resta, '*': multiplicacion, '/': division }


class Simbolo:

	def __init__(self, tipo, valor):
		self.tipo = tipo
		self.valor = valor


	def __str__(self):
		return "Simbolo({},{})".format(self.tipo, self.valor)


def tipoDeOperador(oper):
	return TipoDeSimbolo.operadores[oper]     #Regresa el tipo de Simbolo para cada caracter


class Analizador:

	def __init__(self, texto):
		self.texto = texto    #Texto a ser analizado
		self.puntero = 0    #Posicion del puntero en el texto de entrada


	def analizar(self):    #Identificar simbolos, construir expresion, resolver
		expresion = self.compilarExpresion()
		return expresion


	def compilarExpresion(self): #Procesar texto para construir la expresion
		primerOperando, operator, segundoOperando = self.Simbolizar()
		return SimplificarExpresion(primerOperando, operator, segundoOperando)


	def Simbolizar(self):   #Convierte la expresión en simbolos con el formato numero -> operando -> numero
		primerOperando = self.cargarSiguienteSimbolo()
		self.verificar(primerOperando, [TipoDeSimbolo.numero])

		operator = self.cargarSiguienteSimbolo()		
		self.verificar(operator, [TipoDeSimbolo.suma, TipoDeSimbolo.multiplicacion, TipoDeSimbolo.division, TipoDeSimbolo.resta])

		segundoOperando = self.cargarSiguienteSimbolo()		
		self.verificar(segundoOperando, [TipoDeSimbolo.numero])

		return primerOperando, operator, segundoOperando


	def cargarSiguienteSimbolo(self):   #Carga el siguiente Simbolo en el texto procesado
		caracterActual = self.cargarSiguienteCaracter()		
		
		memoriaNumeral = ''
		while caracterActual is not None and caracterActual.isdigit():
			memoriaNumeral += caracterActual
			caracterActual = self.cargarSiguienteCaracter()

		if len(memoriaNumeral) > 0:
			self.puntero -= 1		
			return Simbolo(TipoDeSimbolo.numero, int(memoriaNumeral))	

		if self.esOperador(caracterActual):			
			return Simbolo(tipoDeOperador(caracterActual), caracterActual)

		raise Exception("Error: La expresión está mal denotada.")


	def esOperador(self, caracter): #Revisar si el caracter cargado es un operador	
		return caracter in TipoDeSimbolo.operadores
	

	def cargarSiguienteCaracter(self):    #Cargar el siguiente caracter de la expresion	
		if self.puntero > len(self.texto) - 1:
			return None

		caracterActual = self.texto[self.puntero]		
		self.puntero += 1
		if caracterActual == ' ':
			caracterActual = self.cargarSiguienteCaracter()	
					
		return caracterActual


	def verificar(self, Simbolo, tipo): #revisar si el Simbolo es valido
		if Simbolo.tipo not in tipo:
			raise Exception("Error: solamente eso, un simple error. Como lo fue enamorarme de ella :'(")

class Interprete:

	def __init__(self, texto):
		self.analizador = Analizador(texto)


	def interpretar(self):
		expresionEntrada = self.analizador.analizar()
		return expresionEntrada.resolver()

class SimplificarExpresion:

	def __init__(self, primerOperando, operator, segundoOperando):   #Numeros son operandos, diferenciar de operadores
		self.primerOperando = primerOperando
		self.operator = operator
		self.segundoOperando = segundoOperando


	def resolver(self):    #Resolver la expresion ya procesada
		identificarOperadores = { 'suma': operator.add, 'resta': operator.sub, 'multiplicacion': operator.mul, 'division': operator.div }

		return identificarOperadores[self.operator.tipo](self.primerOperando.valor, self.segundoOperando.valor)
