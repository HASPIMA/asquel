# [ASQUEL](https://asquelito.tumblr.com/) 0.1
##### Lenguaje de programación orientado a matemáticas

Un nuevo lenguaje de programación creado por el estudiante mexicano de ingeniería industrial y de sistemas [Alan Zatarain](http://zatarain.co.nf/). Está pensado para ser implementado en clases básicas de programación en la Universidad Autónoma de Ciudad Juárez (UACJ). 

## Índice

- [Bases](#bases)
- [Uso práctico](#uso-practico)
- [Documentación](#documentacion)
- [Copyright y licencia](#copyright-y-licencia)

## Bases

Lo primero que hace falta aclarar es que el lenguaje aún no tiene una versión mayor lanzada, solamente las versiones de planeación y esta que es una versión para desarrolladores, pensada para tener código fácil de leer antes que ser útil como programa.
Debe tener dos elementos principales: funciones y tener sintaxis matemática.

### Entonces, ¿Qué diablos hace esta versión?

La versión actual de asquel es un ejemplo de como funciona su analizador de expresiones, tomando como base expresiones matemáticas simples, operaciones aritméticas simples de dos cantidades.

Aquí está un ejemplo de sesión de asquel resolviendo cuatro operaciones:
```
Copyright (c)2017 Alan Ramirez Zatarain
https://soyzatarain.github.io/LICENSE

Asquelito$ 12/3
4

Asquelito$ 832*9
7488

Asquelito$ 845-2
843

Asquelito$ 82743+21
82764

Asquelito$ texto
Error: La expresión está mal denotada.

Asquelito$ 

```
Como se puede observar, al ingresar cualquier otra cosa que no sea un número o un operador aritmético arroja un error.


## Uso práctico

Asquel en este momento no hace nada que una calculadora de cinco dólares no pueda hacer, por lo que realmente un uso práctico está descartado. Su uso es más bien didáctico para el fin que nos ocupa, que es entender la rutina mediante la cual los componentes de una expresión se separan en su forma más simple y se convierten en simbolos que el intérprete puede manejar.
En el siguiente lanzamiento se piensa agregar incógnitas y variables, es algo que se persigue desde las versiones de planeación y creo poder hacerlos mediante diccionarios, pero no se me ha ocurrido una manera simple que sea solamente `variable = 1` y no `variable(nombre, 1)`.


## Documentación

En orden para descargar la última versión estable de asquel puedes dirigirte a nuestro [sitio oficial](https://asquelito.tumblr.com/), donde encontrarás las últimas noticias, actualizaciones y debate en general. Si gustas hacer preguntas, o necesitas soporte para hacer alguna obra derivada de asquel, ese es tu destino.

### Quiero la licencia, los reportes, la bitácora de cambios, etc.

Puedes obtener los documentos uno por uno, o todos en paquete en el sitio oficial. Todas las versiones de asquel (incluidas las de planeación) vienen empaquetadas con toda la documentación disponible en el momento.

## Copyright y licencia

©2017 [Alan Ramirez Zatarain](http://zatarain.co.nf). Asquel es cedido al público bajo la licencia de código abierto zatarain.

