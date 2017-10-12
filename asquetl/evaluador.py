from asquetl import *
import sys

class Evaluador:
    def __init__(object):
        if object == None:
            sys.exit()
        pass

    def evaluar(self, nivel):
        self.variables = {}
        self.resultadoParcial = ""
        self.resolverNivel(nivel)
        return self.resultadoParcial

    def cargarPrograma(self, nivel):
        for declaracion in nivel.modificadores:
            declaracion.cargar(self)

    def resolverNivel(self, nivel):
        try:
            return nivel.cargar(self)
        except AttributeError:
            raise ValueError("Error 003")

    def primeraPrioridad(self, nivel):
        try:
            nivel1 = self.resolverNivel(nivel.primerNum)
            nivel2 = self.resolverNivel(nivel.segundoNum)
        except AttributeError:
            raise ValueError("Error 004")
        if nivel.valor == "*":
            return nivel1 * nivel2
        elif nivel.valor == "/":
            return nivel1 / nivel2
        else:
            raise ValueError("Error 005")

    def segundaPrioridad(self, nivel):
        try:
            nivel1 = self.resolverNivel(nivel.primerNum)
            nivel2 = self.resolverNivel(nivel.segundoNum)
        except AttributeError:
            raise ValueError("Error 004")
        if nivel.valor == "+":
            return nivel1 + nivel2
        elif nivel.valor == "-":
            return nivel1 - nivel2
        else:
            raise ValueError("Error 006")

    def cargarNivelAnidado(self, nivel):
        if not isinstance(nivel.primerNum, puntualizarEslabon):
            raise ValueError("Error 008")
        try:
            nivel1 = nivel.primerNum.valor
            nivel2 = self.resolverNivel(nivel.segundoNum)
        except AttributeError:
            raise ValueError("Error 004")
        self.variables[nivel1] = nivel2

    def funcion(self, nivel):
        if not isinstance(nivel.primerNum, puntualizarEslabon):
            raise ValueError("Error 009")
        try:
            nombreDeLaFuncion = nivel.primerNum.valor
            modificador = self.resolverNivel(nivel.segundoNum)
        except AttributeError:
            raise ValueError("Error 004")
        if nombreDeLaFuncion == "imprimir":
            self.resultadoParcial += str(modificador) + "\n"
        else:
            raise ValueError("Error 010")

    def cargarPorIndice(self, nivel):
        try:
            return self.variables[nivel.valor]
        except KeyError:
            raise ValueError("Error 005")

    def cargarPorValor(self, nivel):
        try:
            return int(nivel.valor)
        except ValueError:
            raise ValueError("Error 006")
