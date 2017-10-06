#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# asquel.py - Interface de entrada y salida standard al usuario
# El presente documento es parte del proyecto Asquel, cedido
# a todo el mundo bajo la LICENCIA COMUN DE CODIGO ABIERTO ZATARAIN.
# Puedes encontrar una copia en doc/LICENSE o en https://github.com/SoyZatarain/asquel/blob/master/doc/LICENSE
#
# Copyright (c)2017 Alan Ramirez Zatarain.

import sys # Esto es para poder obtener los parametros
from asquetl import Diccionario # La clase que procesa todo

def procesar(contenidoDelArchivo): # Esta funcion conecta el archivo de entrada con asquetl.Diccionario
    return Diccionario().lex(contenidoDelArchivo) # Devuelve la matriz de resultados


if __name__ == '__main__': # Si es ejecutado directamente
    if len(sys.argv) == 2: # Si el usuario ingreso dos parametros
        if sys.argv[1].endswith(".asq", 0): # Si la extension de archivo es .ASQ 
            print(procesar(open(sys.argv[1], "r").read())) # Imprimir lo que la funcion procesar() devuelva
        else: # Si la extension del archivo no es .ASQ
            print(sys.argv[1], "no es un documento de Asquel") # Imprimir este aviso
    else: # Si el usuario ingreso uno o mas de 2 parametros
        print("Asquel interpreter 0.2c\nCopyright 2017 Alan Ramirez Zatarain\nhttps://raw.githubusercontent.com/SoyZatarain/asquel/master/doc/LICENSE\n\nUso: ./asquel.py archivo.asq") #Avisos
