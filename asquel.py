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

def procesar(contenidoDelArchivo): # Esta funcion conecta el archivo de entrada con asquetl.*
    matrizDeSimbolos = Diccionario().lex(contenidoDelArchivo) # Generar matriz de valores convertidos a simbolos y su tipo asignado
    diagramaDeNiveles = Analizador().analizar(matrizDeSimbolos) # Generar niveles de jerarquia de resolucion para devolver un diagrama de arbol
    resultado = Evaluador().evaluar(diagramaDeNiveles) # Resuelve los niveles uno por uno hasta llegar al fondo
    return resultado # Devuelve todas las salidas, por ahora solo posibles con imprimir()

if __name__ == '__main__': # Si es ejecutado directamente
    if len(sys.argv) == 2: # Si el usuario ingreso dos parametros
        if sys.argv[1].endswith(".asq", 0): # Si la extension de archivo es .ASQ
            salida = procesar(open(sys.argv[1], "r").read()) # Abrimos el archivo y lo convertimos en contenido apto para mandarlo a asquetl.Diccionario
            print(salida) # Imprimir lo que la funcion procesar() devuelva
        else: # Si la extension del archivo no es .ASQ
            print(sys.argv[1], "no es un documento de Asquel") # Imprimir este aviso
    elif len(sys.argv) == 3:
        opcion = sys.argv[1]
        archivo = open(sys.argv[2], "r").read()
        if opcion == "-d" or opcion == "--diccionario":
            print(Diccionario().lex(archivo))
        elif opcion == "-a" or opcion == "--arbol":
            print(Analizador().analizar(Diccionario().lex(archivo)))
        else:
            print("Opcion invalida: %s" % opcion)
    else: # Si el usuario ingreso uno o mas de 2 parametros
        print("Asquel interpreter 1.0\nCopyright 2017 Alan Ramirez Zatarain\nhttps://raw.githubusercontent.com/SoyZatarain/asquel/master/doc/LICENSE\n") #Avisos
        if sys.argv[0] == "asquel.py" or sys.argv[0] == "./asquel.py":
            programa = "python3 asquel.py"
        else:
            programa = "asquel"
        print("Uso: %s [opcion] <archivo.asq>\n" % programa) #Avisos
        print("  Opciones:")
        print("  -d, --diccionario      Muestra asignación de tipo a los simbolos")
        print("  -a, --arbol            Muestra arbol de sintaxis abstracta")
