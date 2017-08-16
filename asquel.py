#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# asquel.py
# Interface for the user
# Standard input and output.
#
# This is part of the Asquel project.
# (c)2017 Alan Ramirez Zatarain
# https://github.com/SoyZatarain/asquel
#

from xolo import *

limpiar()
derechos()

class Parsero(object):

    if os.name == "posix":
        recolector = chr(27)+"[1;32m"+"Asquelito$ "+chr(27)+"[0;37m"
        error = chr(27)+"[0;91m"+"Error: La expresión está mal denotada."+chr(27)+"[0;37m"+"\n"
    else:
        recolector = "Asquelito/:> "
        error = "Error: La expresión está mal denotada.\n"

    def asquelito(self):
        while True:
            try:
                expresion = raw_input(self.recolector)
                parcial = Interprete(expresion)
                if os.name == "posix":
                    print(chr(27)+"[1;37m"+"%i\n" % parcial.interpretar())
                else:
                    print("%i\n" % parcial.interpretar())
            except EOFError:
                break
            except:
                print(self.error)

if __name__ == "__main__":
    Parsero().asquelito()
