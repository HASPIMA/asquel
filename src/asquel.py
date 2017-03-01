#!/usr/bin/env python
# -*- coding: utf-8 -*-
import parser
from xoloitzcuintle import *

clear()
derechos()

class Parsero(object):
    PROMPT = chr(27)+"[1;32m"+"Asquelito$ "+chr(27)+"[0;37m"
    ALERTA = "Error: La expresión está mal denotada.\n"

    def asquelito(self):
        while True:
            try:
                resultado = evaluar(self.PROMPT)
                print(chr(27)+"[1;37m""{}\n".format(resultado)+chr(27)+"[0;37m")
            except EOFError:
                print('')
                break
            except:
                print(chr(27)+"[0;91m"+self.ALERTA+chr(27)+"[0;37m")

if __name__ == "__main__":
    Parsero().asquelito()
