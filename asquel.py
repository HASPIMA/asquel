#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# asquel.py - Interface de entrada y salida standard al usuario
# El presente documento es parte del proyecto Asquel, cedido
# a todo el mundo bajo la LICENCIA COMUN DE CODIGO ABIERTO ZATARAIN.
# Puedes encontrar una copia en doc/LICENSE o en https://raw.githubusercontent.com/SoyZatarain/asquel/master/doc/LICENSE
#
# Copyright (c)2017 Alan Ramirez Zatarain.

import sys # Esto es para poder obtener los parametros
from asquetl import * # Las clases que procesan todo
from asquetl.evaluador import Evaluador

def procesar(contenidoDelArchivo): # Esta funcion conecta el archivo de entrada con asquetl.Diccionario y luego con asquetl.Analizador
    matrizDeSimbolos = Diccionario().lex(contenidoDelArchivo) # Generar matriz de valores convertidos a simbolos y su tipo asignado
    resultado = Evaluador().evaluar(Analizador().analizar(matrizDeSimbolos)) # Genera el arbol procesado con la jerarquia de niveles
    return resultado # Devuelve todas las salidas, por ahora solo posibles con imprimir()


if __name__ == '__main__': # Si es ejecutado directamente
    print("Asquel interpreter 0.99rc1\nCopyright 2017 Alan Ramirez Zatarain\nhttps://raw.githubusercontent.com/SoyZatarain/asquel/master/doc/LICENSE\n") #Avisos
    if len(sys.argv) == 2: # Si el usuario ingreso dos parametros
        if sys.argv[1].endswith(".asq", 0): # Si la extension de archivo es .ASQ 
            salida = procesar(open(sys.argv[1], "r").read()) # Abrimos el archivo y lo convertimos en contenido apto para mandarlo a asquetl.Diccionario
            print(salida) # Imprimir lo que la funcion procesar() devuelva
        else: # Si la extension del archivo no es .ASQ
            print(sys.argv[1], "no es un documento de Asquel") # Imprimir este aviso
    else: # Si el usuario ingreso uno o mas de 2 parametros
        print("Uso: [python3] asquel.py <archivo.asq>\n") #Avisos
