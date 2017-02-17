# -*- coding: utf-8 -*-

print 'Asquel versión 0.0.0.0b'
print 'Copyright 2017 Alan Ramirez Zatarain'
print 'Liberado al público bajo la BSD 3-Clause License'
print 'Para aprender sobre la sintaxys de asquel ingresa a:'
print 'http://asquel.hol.es/'
print ' '


def testu():
    while True:
        try:
            entrada = raw_input('asquelito$ ')
        except EOFError:
            break
        if not entrada:
            continue
	print '%s\n' % entrada


if __name__ == '__main__':
    testu()
