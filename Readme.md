
<h1 align="center">
  <br>
  <a href="https://asquelito.tumblr.com/"><img src="https://raw.githubusercontent.com/SoyZatarain/asquel/master/icono.png" alt="Asquelito" width="200"></a>
  <br>
  Asquel 0.99rc1
  <br>
</h1>

<h4 align="center">Lenguaje de programación extremadamente fácil para introducir conceptos básicos en clases universitarias.</h4>

<p align="center">
  <a href="https://asquelito.tumblr.com/">
    <img src="https://img.shields.io/badge/Estado-Estable-green.svg">
  </a>
  <a href="https://asquelito.tumblr.com/"><img src="https://img.shields.io/badge/Versi%C3%B3n-0.99rc1-green.svg"></a>
</p>
<br>

## ¿Qué es Asquel?
Asquel es un nuevo lenguaje de programación con la intención de ser usado como material didáctico en clases univesitarias de fundamentos de programación, como primer lenguaje de programación para estudiantes que quieran empezar a escribir código. Normalmente para esta tarea se emplean lenguajes muy complejos para un principiante, como Java o C#, lo que confunde al estudiante y genera un repudio a seguir programando luego de cumplir con la materia. Asquel tiene una sintaxis muy sencilla, pero conservando algunos elementos de lenguajes superiores para que los alumnos aprendan y conserven estos hábitos de escritura estricta. No se pretende crear un lenguaje complejo a nivel de python o perl, se renuncia a varios elementos de los lenguajes habituales para que los alumnos puedan aprender de a poco.
Una vez conquistado asquel, la transición a lenguajes más completos como Python o C es notablemente más fácil.

## Ejemplo de programa hecho en Asquel
```
a = 1 + 1 * 8 - 9 / 6 / 17;
b = 7;
a = a + b;
imprimir(a + 1);
```
En la primera línea vemos la asignación de la variable "a" con una expresión compleja.
En la segunda asignamos la variable "b" igual a 7.
En la tercera línea re asignamos la variable "a" como el resultado de sumar ella misma más "b".
Finalmente nuestra primera fucnión estándar, imprimir().
Como se puede apreciar, se usa punto y coma (;) como separador de declaraciones, principalmente para que los estudiantes se acostumbren a este tipo de elementos obligatorios.

## Modo de uso

Asquel funciona de manera muy similar (o identica) a interpretes ya conocidos. Es a través de una línea de comandos, invocando a python a ejecutar asquel, e indicándole a éste último que cargue un archivo, de la siguiente forma:
`python asquel.py nombre-del-archivo.asq`
Asquel devolverá el resultado del programa que se haya introducido, por ahora la única función que puede interactuar con la salida estándar es imprimir().
Aquí se muestra un ejemplo de ejecución de Asquel procesando el programa "prueba.asq" incluido en la carpeta "ejemplos":

```
alan@alan-PC:~/asquel$ ./asquel.py prueba.asq
Asquel interpreter 0.99rc1
Copyright 2017 Alan Ramirez Zatarain
https://raw.githubusercontent.com/SoyZatarain/asquel/master/doc/LICENSE

16.911764705882355

alan@alan-PC:~/asquel$ 

```
El 16.9117... aparece porque hay una llamada a imprimir() dentro de prueba.asq y lo que se muestra es el resultado de procesar sus parametros.
Por ahora imprimir() sólo procesa expresiones matemáticas, pero ya se trabaja en incluir cadenas de texto.

## En esta versión:

* Programas ya pueden ser procesados y arrojar resultados a salida con imprimir()
* Completa integración de las clases incluidas en asquetl
* Asquel ya se puede considerar un lenguaje de programación y se encuentra a pocos pasos de alcanzar la meta de ser apto para instruir a los alumnos en fundamentos de programación.


## Descarga
### Última versión estable:
[Asquel 0.1.13](https://sourceforge.net/projects/asquel-old/files/asquel-0.1.3.zip/download) es la mejor versión de asquel, es anterior al cambio de modelo y tiene todas las caracteristicas que se habían conseguido como el modo interactivo, analisis de archivos, gestor de errores entre otros, pero carece de sintaxis, sólo procesa expresiones matemáticas.
### Versión actual:
- Puedes clonar este repositorio con `git clone git://github.com/SoyZatarain/asquel.git`
- Tambien puedes dar clic [aquí](https://github.com/SoyZatarain/asquel/archive/master.zip) para descargar el paquete a través del navegador.
### Versiones anteriores:
Puedes descargar desde la versión 0.0, 0.1, etc. de [esta lista](https://sourceforge.net/projects/asquel-old/files/) alojada por SourceForge.

## Desarrollo futuro

* Extender las funciones estándar
* Añadir cadenas a imprimir()
* Mudarnos a C++

## Licencia

La licencia que cubre a Asquel está en doc/LICENSE o en [este enlace](https://raw.githubusercontent.com/SoyZatarain/asquel/master/doc/LICENSE).

---

> [Alan Zatarain](https://soyzatarain.github.io/) &nbsp;&middot;&nbsp;
> [Facebook](https://www.facebook.com/SoyZatarain/) &nbsp;&middot;&nbsp;
> Twitter [@SoyZatarain](https://twitter.com/SoyZatarain)

