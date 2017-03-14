#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from xoloitzcuintle import *

clear()
derechos()

class Parsero(object):
    if os.name == "posix":
        PROMPT = chr(27)+"[1;32m"+"Asquelito$ "+chr(27)+"[0;37m"
        ALERTA = chr(27)+"[0;91m"+"Error: La expresión está mal denotada."+chr(27)+"[0;37m"+"\n"
    else:
        PROMPT = "Asquelito$ "
        ALERTA = "Error: La expresión está mal denotada.\n"

    def asquelito(self):
        while True:
            try:
                resultado = evaluar(self.PROMPT)
                if os.name == "posix":
                    print(chr(27)+"[1;37m""{}\n".format(resultado)+chr(27)+"[0;37m")
                else:
                    print("{}\n".format(resultado))
            except EOFError:
                break
            except:
                print(self.ALERTA)

if __name__ == "__main__":
    Parsero().asquelito()
