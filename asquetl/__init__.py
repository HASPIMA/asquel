# asquetl/__init__.py - Modulo de funciones internas de Asquel
# El presente documento es parte del proyecto Asquel, cedido
# a todo el mundo bajo la LICENCIA COMUN DE CODIGO ABIERTO ZATARAIN.
# Puedes encontrar una copia en doc/LICENSE o en https://raw.githubusercontent.com/SoyZatarain/asquel/master/doc/LICENSE
#
# Copyright (c)2017 Alan Ramirez Zatarain.

from abc import ABC, abstractmethod
import re

class Diccionario:

    def __init__(self):
        simbolos = [
            ("numero", "[0-9]+"),
            ("primeraPrioridad", "\*|/"),
            ("segundaPrioridad", "\+|-"),
            ("parentesis", "\(|\)"),
            ("nombre", "[A-Za-z][A-Za-z0-9]*"),
            ("igual", "="),
            ("espacio", "\s+"),
            ("separador", ";"),
            ("nada", "Null")
        ]

        concatenado = '|'.join("(?P<{}>{})".format(tipo, valor) for (tipo, valor) in simbolos)
        self.expresion = re.compile(concatenado)

    def lex(self, cadena):
        simbolos = []
        posicion = 0
        simbolo = self.expresion.match(cadena)
        while simbolo:
            tipo = simbolo.lastgroup
            valor = simbolo.group(tipo)
            if tipo != "espacio":
                simbolos.append((valor, tipo))
            posicion += len(valor)
            simbolo = self.expresion.match(cadena, posicion)
        if posicion < len(cadena):
            raise ValueError("Error 001")
        return simbolos

class Analizador:

	def analizar(self, simbolos):
		self.simbolos = simbolos
		self.posicion = 0
		self.simbolizar()
		fondo = Cadena()
		fondo.modificadores = [self.dividirDeclaracion()]
		while self.simbolo[1] != "EOF":
			fondo.modificadores.append(self.dividirDeclaracion())
		return fondo


	def comparar(self, *valorEsperado):
		if self.simbolo[1] not in valorEsperado:
			raise ValueError("Error 002: se esperaba " + str(valorEsperado) + ". pero se encontro " + self.simbolo[1])


	def simbolizar(self):
		try:
			self.simbolo = self.simbolos[self.posicion]
		except IndexError:
			self.simbolo = (None, "EOF")
		self.posicion += 1


	def dividirDeclaracion(self):
		self.comparar("nombre")
		nombreDelSimbolo = self.simbolo
		self.simbolizar()
		self.comparar("igual", "parentesis")
		if self.simbolo[1] == "igual":
			fondo = contraFondo()
			fondo.primerNum = puntualizarEslabon(nombreDelSimbolo[0])
			self.simbolizar()
			fondo.segundoNum = self.convertirTermino()
		elif self.simbolo[1] == "parentesis":
			fondo = saltarAEslabon()
			fondo.primerNum = puntualizarEslabon(nombreDelSimbolo[0])
			self.simbolizar()
			fondo.segundoNum = self.convertirTermino()
			self.comparar("parentesis")
			self.simbolizar()
		self.comparar("separador")
		self.simbolizar()
		return fondo


	def convertirTermino(self):
		fondo = self.convertirFactor()
		while self.simbolo[1] == "segundaPrioridad":
			fondoDelEslabon = agregarEslabon(self.simbolo[0])
			self.simbolizar()
			numero = self.convertirFactor()
			fondoDelEslabon.primerNum = fondo
			fondoDelEslabon.segundoNum = numero
			fondo = fondoDelEslabon
		return fondo


	def convertirFactor(self):
		fondo = self.analizarPorValor()
		while self.simbolo[1] == "primeraPrioridad":
			fondoDelEslabon = agregarNivel(self.simbolo[0])
			self.simbolizar()
			valor = self.analizarPorValor()
			fondoDelEslabon.primerNum = fondo
			fondoDelEslabon.segundoNum = valor
			fondo = fondoDelEslabon
		return fondo


	def analizarPorValor(self):
		self.comparar("nombre", "numero")
		if self.simbolo[1] == "nombre":
			fondo = puntualizarEslabon(self.simbolo[0])
		elif self.simbolo[1] == "numero":
			fondo = cima(self.simbolo[0])
		self.simbolizar()
		return fondo

class Nivel(ABC):

	@abstractmethod
	def cargar(self, enlazador):
		pass

	def __eq__(self, diferente):
		return isinstance(diferente, self.__class__) and (self.valor == diferente.valor)

	def __str__(self, objetivoDeApuntador=0):
		return "\t" * objetivoDeApuntador + repr(self.valor) + "\n"


class Cadena(Nivel):
	def __init__(self):
		self.valor = "asquelito"
		self.modificadores = []

	def cargar(self, enlazador):
		return enlazador.cargarPrograma(self)

	def __eq__(self, diferente):
		return (super(Cadena, self).__eq__(diferente) and 
			self.modificadores == diferente.modificadores)

	def __str__(self, objetivoDeApuntador=0):
		puntoDeRetorno = super(Cadena, self).__str__(objetivoDeApuntador)
		for modificador in self.modificadores:
			puntoDeRetorno += modificador.__str__(objetivoDeApuntador+1)
		return puntoDeRetorno


class puntualizarEslabon(Nivel):
	def __init__(self, valor):
		self.valor = valor

	def cargar(self, enlazador):
		return enlazador.cargarPorIndice(self)


class cima(Nivel):
	def __init__(self, valor):
		self.valor = valor

	def cargar(self, enlazador):
		return enlazador.cargarPorValor(self)

class nivelComputado(Nivel, ABC):
	def __init__(self):
		self.primerNum = None
		self.segundoNum = None

	def __eq__(self, diferente):
		return (super(nivelComputado, self).__eq__(diferente) and 
			self.primerNum == diferente.primerNum and
			self.segundoNum == diferente.segundoNum)

	def __str__(self, objetivoDeApuntador=0):
		puntoDeRetorno = super(nivelComputado, self).__str__(objetivoDeApuntador)
		puntoDeRetorno += self.primerNum.__str__(objetivoDeApuntador+1)
		puntoDeRetorno += self.segundoNum.__str__(objetivoDeApuntador+1)
		return puntoDeRetorno


class agregarEslabon(nivelComputado):
	def __init__(self, valor):
		super(agregarEslabon, self).__init__()
		self.valor = valor

	def cargar(self, enlazador):
		return enlazador.segundaPrioridad(self)


class agregarNivel(nivelComputado):
	def __init__(self, valor):
		super(agregarNivel, self).__init__()
		self.valor = valor

	def cargar(self, enlazador):
		return enlazador.primeraPrioridad(self)


class contraFondo(nivelComputado):
	def __init__(self):
		self.valor = "igual"

	def cargar(self, enlazador):
		return enlazador.cargarNivelAnidado(self)


class saltarAEslabon(nivelComputado):
	def __init__(self):
		self.valor = "funcion"

	def cargar(self, enlazador):
		return enlazador.funcion(self)
