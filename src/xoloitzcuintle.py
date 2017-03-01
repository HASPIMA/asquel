#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import *
import sys
import os

def gradarad(x):			#Convertir de grados a radianes
	pi = 3.141592			#Prefijo GAR:
	e = 2.718281
	return (x*pi/180)

def radagrad(x):			#Convertir de radianes a grados
	return ((x*180)/pi)		#Prefijo RAG:

def exp(x):			#valor de e elevado a a la x potencia
	return e**x			#Prefijo EXP:

def pot(x, y):			#valor de x a la y potencia
	return x**y			#Prefijo POT:

def hipotenusa(x, y):		#hipotenusa segun norma euclideana rz2(x*x + y*y)
	return rz2((x*x)+(y*y))	#Prefijo HIP:

def rz2(number):			#Raiz cuadrada de x
    if(number == 0):			#Prefijo RZ2:
        return 0;

    g = number/2.0;
    g2 = g + 1;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g + n)/2;

    return g;

def vabs(x):			#valor absoluto de x
	return rz2(x*x)		#Prefijo VAB:

def suelo(x):			#Menor numero entero inmediato, menor o igual a x
	return (x-(x%1))		#Prefijo SLO:

def techo(x):			#Mayor numero entero inmediato, mayor o igual a x
	return (suelo(x)+1)		#Prefijo TCH:

def cpsg(x, y):			#Copia el signo de y a x
	s = 0				#Prefijo CPS:
	if y < 0:			#XXX esto va a dar bug, corregirlo.
		s = -1
	else:
		s = 1

	return (x*s)

def fact(n):			#Factorial de un numero (fact(5) = 1*2*3*4*5 = 120)
    num = 1				#Prefijo FCT:
    while n >= 1:
        num = num * n
        n = n - 1
    return num

def seno(x):			#Funcion trigonometrica seno
	if x == 90:			#Prefijo SEN:
		return 1
	else:
		org = gradarad(x)
		res = (org-((org**3)/fact(3))+((org**5)/fact(5))-((org**7)/fact(7)))
		return res

def coseno(x):			#Funcion trigonometrica coseno
	org = gradarad(x)			#Prefijo COS:
	res = (1-((org**3)/fact(3))+((org**5)/fact(5))-((org**7)/fact(7)))
	return cos(gradarad(x))

def tangente(x):			#Funcion trigonometrica tangente
	tang = seno(x)/(rz2(1-(seno(x)**2)))	#Prefijo TAN:
	return tang

def descx(x, y):			#descomponer en el eje X vector de x fuerza a y grados del eje X poritivo
	return x*coseno(y)		#Prefijo DSX:

def descy(x, y):			#descomponer en el eje Y vector de x fuerza a y grados del eje X positivo
	return x*seno(y)		#Prefijo DSY:

#def lb10(x):			#logaritmo en base 10 de x
#	return log10(x)
#
def invtan(x):			#tangente^-1(x)
	return radagrad(atan(x))

def invcos(x):			#coseno^-1(x)
	return radagrad(acos(x))

def invsen(x):			#seno^-1(x)
	return radagrad(asin(x))

def derechos():			#Burocracia
	print(chr(27)+"[1;33m"+'Asquel versión 0.0.0.0d')	#[version mayor].[version menor].[compilacion].[prueba]
	print('Copyright (c)2017 Alan Ramirez Zatarain')	#Hello, my name is Alan.
	print('Puedes obtener información sobre la licencia en')	#Debo mantener esto aqui?
	print('http://asquel.hol.es/LICENSE\n'+chr(27)+"[0;37m")	#Solo actualizaciones, no cambios de licencia

if sys.version_info[0] < 3:	#revisar que version de python esta ejecutando, en caso de ser menor de 3...
    def evaluar(prompt):	#funcion para cargar lo escrito por el usuario
        return input(prompt)	#denotacion de python 2.x
else:	#caso contrario, que si sea 3 o superior...
    def evaluar(prompt):
        return eval(input(prompt))	#denotacion para python 3.x

def clear():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")
