#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# asquel.py - Interface de entrada y salida standard al usuario
# El presente documento es parte del proyecto Asquel, cedido
# a todo el mundo bajo la LICENCIA COMUN DE CODIGO ABIERTO ZATARAIN.
# Puedes encontrar una copia en doc/LICENSE o en https:://soyzatarain.github.io/LICENSE
#
# Copyright (c)2017 Alan Ramirez Zatarain.

from xolo import *

limpiar()
derechos()

def main():

    if os.name == "posix":
        recolector = chr(27)+"[1;32m"+"Asquelito:~$ "+chr(27)+"[0;37m"
        error = chr(27)+"[0;91m"+" Error: La expresión está mal denotada."+chr(27)+"[0;37m"+"\n"
    else:
        recolector = "Asquelito:/> "
        error = " Error: La expresión está mal denotada.\n"

    while True:
        try:
            try:
                texto = raw_input(recolector)
            except NameError:
                texto = input(recolector)
            except SyntaxError:
                continue

            resultado = Resolucion(Analizador(Procesar(texto))).resolver()

            if os.name == 'posix':
                print(chr(27)+"[1;37m", resultado, "\n")
            else:
                print(resultado)

        except EOFError:
            break

        except:
            if not texto:
                continue
            else:
                print(error)
                continue

if __name__ == '__main__':
    main()
