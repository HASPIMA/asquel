# -*- coding: utf-8 -*-
import parser
from math import *

print 'Asquel versión 0.0.0.0c'
print 'Copyright 2017 Alan Ramirez Zatarain'
print 'Liberado al público bajo la BSD 3-Clause License'
print 'Para aprender sobre la sintaxys de asquel ingresa a:'
print 'http://asquel.hol.es/'
print ' '


def main():
    while True:
        try:
            entrada = raw_input('asquelito$ ')
        except EOFError:
            break
        if not entrada:
            continue

	medio = parser.expr(entrada).compile()
	resultado = eval(medio)
	print '%s\n' % resultado

if __name__ == '__main__':
    main()
