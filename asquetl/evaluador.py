from asquetl import *
import sys

class Evaluador:                # Nuestro objeto
    def __init__(object):       # El respectivo constructor
        if object == None:      # En caso de que no recibamos el preprocesado
            sys.exit()          # El programa abortará para que no se quede en un loop infinito
        pass

    def evaluar():              # La función principal, lo que finalmente generará la salida, haciendo uso de las siguientes funciones secundarias:
        pass

    def cargarPrograma():       # Separa al programa preprocesado en líneas que se pueden ejecutarse como pasos consecutivos
        pass

    def resolverNivel():        # Ir eliminando los niveles que ya estén en su forma final y lanzarlos al inferior
        pass

    def primeraPrioridad():     # Resolver expresiones
        pass

    def segundaPrioridad():     # Resolver expresiones
        pass

    def cargarNivelAnidado():   # Un nivel dentro de otro nivel por ejemplo imprimir(1+2/7-8);
        pass

    def funcion():              # Funciones declaradas como imprimir()
        pass
