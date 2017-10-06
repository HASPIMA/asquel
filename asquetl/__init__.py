import re # Vamos a usar re.compile(), re.match(), re.lastgroup y re.group(), 

# asquetl/__init__.py - Modulo de funciones internas de Asquel
# El presente documento es parte del proyecto Asquel, cedido
# a todo el mundo bajo la LICENCIA COMUN DE CODIGO ABIERTO ZATARAIN.
# Puedes encontrar una copia en doc/LICENSE o en https://raw.githubusercontent.com/SoyZatarain/asquel/master/doc/LICENSE
#
# Copyright (c)2017 Alan Ramirez Zatarain.

class Diccionario: # "from asquetl import Diccionario" carga toda esta clase
    def __init__(self): # Nuestro constructor
        simbolos = [
            ("numero", "[0-9]+"), #Los numeros de toda la vida (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
            ("primeraPrioridad", "\*|/"), # Primera prioridad a ser resuelta
            ("segundaPrioridad", "\+|-"), # Segunda prioridad a ser resuelta
            ("parentesis", "\(|\)"), # Para operaciones que los incluyan, modificando la jerarquia en pasos
            ("espacio", "\s+") # Espacios " ", no los vamos a tomar en cuenta, pero debemos declararlos para poder saltarlos
        ]
        concatenado = '|'.join("(?P<{}>{})".format(tipo, valor) for (tipo, valor) in simbolos) # Asignar a cada valor un tipo
        self.expresion = re.compile(concatenado)    # Le damos formato

    def lex(self, cadena): # Esta funcion devuelve una tabla ordenada, convirtiendo los valores en simbolos y con su valor asignado
        simbolos = [] # simbolos es una matriz
        posicion = 0 # la posicion es el caracter actual
        simbolo = self.expresion.match(cadena) # tomando en cuenta los parametros del diccionario de simbolos, a cada valor le corresponde un tipo que encaje
        while simbolo: # Mientras haya mas para cargar
            tipo = simbolo.lastgroup # Le asignamos el tipo que encontro con match()
            valor = simbolo.group(tipo) # establecemos que la relacion encontrada sea asignada
            if tipo != "espacio": # Solo cuando el caracter no es un espacio
                simbolos.append((valor, tipo)) # Guardamos el binomio simbolo-tipo en la matriz
            posicion += len(valor) # Avanzamos tantos caracteres como tenga el simbolo procesado para pasar al siguiente
            simbolo = self.expresion.match(cadena, posicion) # Cada simbolo corresponde a un segmento de la cadena procesada, iniciando por su posicion
        if posicion < len(cadena): # Numero de indices incorrecto
            raise ValueError("Error 001") # Solo para depurador, no se imprime a pantalla
        return simbolos # Devolver a estandar
