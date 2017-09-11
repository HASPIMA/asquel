#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# asquel.py - Interface de entrada y salida standard al usuario
# El presente documento es parte del proyecto Asquel, cedido
# a todo el mundo bajo la LICENCIA COMUN DE CODIGO ABIERTO ZATARAIN.
# Puedes encontrar una copia en doc/LICENSE o en https://github.com/SoyZatarain/asquel/blob/master/doc/LICENSE
#
# Copyright (c)2017 Alan Ramirez Zatarain.

from asquetl import *
import sys

derechos()

def asquelito():
    if len(sys.argv) == 2:
        f = open(sys.argv[1], "r")
        i = 0
        for linea in f:
            try:
                i = i + 1
                resultado = Resolucion(Analizador(Procesar(linea))).resolver()
                print(i, resultado)
            except EOFError:
                break

            except:
                if not linea:
                    continue
                else:
                    print("Error en linea", i)
                    continue
        f.close()
        print()

    else:
        while True:
            try:
                try:
                    texto = raw_input("Asquelito>>> ")
                except NameError:
                    texto = input("Asquelito>>> ")
                except SyntaxError:
                    continue

                resultado = Resolucion(Analizador(Procesar(texto))).resolver()
    
                print("%i\n" % resultado)
    
            except EOFError:
                break

            except:
                if not texto:
                    continue
                else:
                    print("Error de denotación\n")
            continue

if __name__ == '__main__':
    asquelito()
