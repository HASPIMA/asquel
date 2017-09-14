import re

class Diccionario:

    def __init__(self):
        simbolos = [
            ("parentesis", "\(|\)"),
            ("segundaPrioridad", "\+|-"),
            ("primeraPrioridad", "\*|/"),
            ("numero", "[0-9]+"),
            ("espacio", "\s+")
        ]

        concatenado = '|'.join("(?P<{}>{})".format(tipo, valor) for (tipo, valor) in simbolos)
        self.expresion = re.compile(concatenado)

    def convertirEnSimbolos(self, cadena):
        simbolos = []
        posicion = 0
        simbolo = self.expresion.match(cadena)

        while simbolo:
            tipo = simbolo.lastgroup
            valor = simbolo.group(tipo)
            if tipo != "espacio":
                simbolos.append(("  "+valor+(" "*(5 - len(valor))), "  "+tipo+(" "*(20 - len(tipo)))))

            posicion += len(valor)
            simbolo = self.expresion.match(cadena, posicion)

        if posicion < len(cadena):
            raise ValueError("Error 001")

        i = 0
        for lineas in simbolos:
            print(simbolos[i])
            i = i + 1
