# xolo/__init__.py - Modulo de funciones internas de Asquel
# El presente documento es parte del proyecto Asquel, cedido
# a todo el mundo bajo la LICENCIA COMUN DE CODIGO ABIERTO ZATARAIN.
# Puedes encontrar una copia en doc/LICENSE o en https://github.com/SoyZatarain/asquel/blob/master/doc/LICENSE
#
# Copyright (c)2017 Alan Ramirez Zatarain.

def derechos():
        print('INterprete Asquel version 0.2a')
        print('Copyright (c)2017 Alan Ramirez Zatarain')
        print('https://github.com/SoyZatarain/asquel/blob/master/doc/LICENSE\n')

NUMERO = 'NUMERO'
MAS = 'MAS'
MENOS = 'MENOS'
POR = 'POR'
ENTRE = 'ENTRE'
ABRE_PARENTESIS = '('
CIERRA_PARENTESIS = ')'
FINAL = 'FINAL'

class Simbolo(object):
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def __str__(self):
        return 'Simbolo({tipo}, {valor})'.format(
            tipo=self.tipo,
            valor=repr(self.valor)
        )

    def __repr__(self):
        return self.__str__()


class Procesar(object):
    def __init__(self, texto):
        self.texto = texto
        self.posicion = 0
        self.caracterActual = self.texto[self.posicion]

    def error(self):
        raise Exception('01')

    def avanzar(self):
        self.posicion += 1
        if self.posicion > len(self.texto) - 1:
            self.caracterActual = None
        else:
            self.caracterActual = self.texto[self.posicion]

    def eliminarEspacios(self):
        while self.caracterActual is not None and self.caracterActual.isspace():
            self.avanzar()

    def numeros(self):
        resultado = ''
        while self.caracterActual is not None and self.caracterActual.isdigit():
            resultado += self.caracterActual
            self.avanzar()
        return int(resultado)

    def siguienteSimbolo(self):
        while self.caracterActual is not None:

            if self.caracterActual.isspace():
                self.eliminarEspacios()
                continue

            if self.caracterActual.isdigit():
                return Simbolo(NUMERO, self.numeros())

            if self.caracterActual == '+':
                self.avanzar()
                return Simbolo(MAS, '+')

            if self.caracterActual == '-':
                self.avanzar()
                return Simbolo(MENOS, '-')

            if self.caracterActual == '*':
                self.avanzar()
                return Simbolo(POR, '*')

            if self.caracterActual == '/':
                self.avanzar()
                return Simbolo(ENTRE, '/')

            if self.caracterActual == '(':
                self.avanzar()
                return Simbolo(ABRE_PARENTESIS, '(')

            if self.caracterActual == ')':
                self.avanzar()
                return Simbolo(CIERRA_PARENTESIS, ')')

            self.error()

        return Simbolo(FINAL, None)

class Estructura(object):
    pass


class DosCantidades(Estructura):
    def __init__(self, izquierda, operador, derecha):
        self.izquierda = izquierda
        self.token = self.operador = operador
        self.derecha = derecha


class ValorSencillo(Estructura):
    def __init__(self, token):
        self.token = token
        self.valor = token.valor


class Cantidad(Estructura):
    def __init__(self, operador, expr):
        self.token = self.operador = operador
        self.expr = expr


class Analizador(object):
    def __init__(self, diccionario):
        self.diccionario = diccionario
        self.simbolo_actual = self.diccionario.siguienteSimbolo()

    def error(self):
        raise Exception('02')

    def cargar(self, tipo_de_simbolo):
        if self.simbolo_actual.tipo == tipo_de_simbolo:
            self.simbolo_actual = self.diccionario.siguienteSimbolo()
        else:
            self.error()

    def factor(self):
        simbolo = self.simbolo_actual
        if simbolo.tipo == MAS:
            self.cargar(MAS)
            nodo = Cantidad(simbolo, self.factor())
            return nodo
        elif simbolo.tipo == MENOS:
            self.cargar(MENOS)
            nodo = Cantidad(simbolo, self.factor())
            return nodo
        elif simbolo.tipo == NUMERO:
            self.cargar(NUMERO)
            return ValorSencillo(simbolo)
        elif simbolo.tipo == ABRE_PARENTESIS:
            self.cargar(ABRE_PARENTESIS)
            nodo = self.expr()
            self.cargar(CIERRA_PARENTESIS)
            return nodo

    def termino(self):
        nodo = self.factor()

        while self.simbolo_actual.tipo in (POR, ENTRE):
            token = self.simbolo_actual
            if token.tipo == POR:
                self.cargar(POR)
            elif token.tipo == ENTRE:
                self.cargar(ENTRE)

            nodo = DosCantidades(izquierda=nodo, operador=token, derecha=self.factor())

        return nodo

    def expr(self):
        nodo = self.termino()

        while self.simbolo_actual.tipo in (MAS, MENOS):
            token = self.simbolo_actual
            if token.tipo == MAS:
                self.cargar(MAS)
            elif token.tipo == MENOS:
                self.cargar(MENOS)

            nodo = DosCantidades(izquierda=nodo, operador=token, derecha=self.termino())

        return nodo

    def procesar(self):
        nodo = self.expr()
        if self.simbolo_actual.tipo != FINAL:
            self.error()
        return nodo

class BajarNivel(object):
    def convertirEnPuntero(self, nodo):
        prefijo = 'apuntar' + type(nodo).__name__
        puntero = getattr(self, prefijo, self.punteroVacio)
        return puntero(nodo)

    def punteroVacio(self, nodo):
        raise Exception('08')


class Resolucion(BajarNivel):
    def __init__(self, selector):
        self.selector = selector

    def apuntarDosCantidades(self, nodo):
        if nodo.operador.tipo == MAS:
            return self.convertirEnPuntero(nodo.izquierda) + self.convertirEnPuntero(nodo.derecha)
        elif nodo.operador.tipo == MENOS:
            return self.convertirEnPuntero(nodo.izquierda) - self.convertirEnPuntero(nodo.derecha)
        elif nodo.operador.tipo == POR:
            return self.convertirEnPuntero(nodo.izquierda) * self.convertirEnPuntero(nodo.derecha)
        elif nodo.operador.tipo == ENTRE:
            return self.convertirEnPuntero(nodo.izquierda) / self.convertirEnPuntero(nodo.derecha)

    def apuntarValorSencillo(self, nodo):
        return nodo.valor

    def apuntarCantidad(self, nodo):
        operador = nodo.operador.tipo
        if operador == MAS:
            return +self.convertirEnPuntero(nodo.expr)
        elif operador == MENOS:
            return -self.convertirEnPuntero(nodo.expr)

    def resolver(self):
        estructura = self.selector.procesar()
        if estructura is None:
            return ''
        return self.convertirEnPuntero(estructura)
