
<h1 align="center">
  <br>
  <a href="https://asquelito.tumblr.com/"><img src="https://raw.githubusercontent.com/SoyZatarain/asquel/master/icono.png" alt="Asquelito" width="200"></a>
  <br>
  Asquel 0.2d
  <br>
</h1>

<h4 align="center">Lenguaje de programación extremadamente fácil para introducir conceptos básicos en clases universitarias.</h4>

<p align="center">
  <a href="https://asquelito.tumblr.com/">
    <img src="https://img.shields.io/badge/Estado-Estable-green.svg">
  </a>
  <a href="https://asquelito.tumblr.com/"><img src="https://img.shields.io/badge/Versi%C3%B3n-0.2d-green.svg"></a>
</p>
<br>

## ¿Qué es Asquel?
Es un lenguaje de programación muy sencillo, con una sintaxis simple y de manejo fácil de aprender a través de una línea de comandos. EStá pensado para servir como primer lenguaje de programación para estudiantes universitarios que recurren a lenguajes más complejos como Java o C# para aprender, lo que resulta contra producente, ya que normalmente en los 6 meses que dura el curso de introducción a la programación no aprenden los conceptos básicos y después tienen problemas en clases superiores, o ya directamente reprueban.
Asquel aún no está terminado, y no persigue el propósito de equipararse a Python o Perl, por ejemplo, sino que apuesta por ser fácil de aprender en menos de un mes y ser el primer escalón de los estudiantes, por eso su sintaxis debe ser minimizada, compacta y fácil de leer.
Asquel está implementado en Python.

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

Asquel se encuentra actualmente en una etapa intermedia entre el algoritmo de procesamiento obsoleto a uno más preciso y con capacidad para procesar los elementos del lenguaje que aún no están disponibles, como las variables, funciones, estructuras, etc.,
Justo ahora, Asquel puede vaciar la estructura de un programa con escrito con su nueva sintaxis recien creada.
Sin embrago, Asquel no está terminado y de hecho, a pesar de que esto representa un avance abismal, aún falta la parte más importante, que es la resolución del programa y la evaluación de expresiones. Una parte de estos dos elementos ya está, pero falta integrarlos, esto tal vez necesite un puente que envíe los datos de expresiones y devuelva el reultado final, solamente inyectándolo en la estructura que ya tenemos. Es teoría todavía, pero todo apunta a que será así.
Para probar como es que Asquel procesa la nueva sintaxis, puedes probarlo con el archivo "prueba.asq" incluido en la carpeta "ejemplos".
`python asquel.py ejemplos/prueba.asq`
Así se vaciará a la salida estándar la estructura resultante de proesar el programa de Asquel con la sintaxis nueva.
Al ejecutar esa orden, Asquel devolvera la estructura del programa, como se muestra más abajo:

```
alan@alan-PC:~/asquel$ ./asquel.py prueba.asq
Asquel interpreter 0.2d
Copyright 2017 Alan Ramirez Zatarain
https://raw.githubusercontent.com/SoyZatarain/asquel/master/doc/LICENSE

'asquelito'
	'igual'
		'a'
		'-'
			'+'
				'1'
				'*'
					'1'
					'8'
			'/'
				'/'
					'9'
					'6'
				'17'
	'igual'
		'b'
		'7'
	'igual'
		'a'
		'+'
			'a'
			'b'
	'funcion'
		'imprimir'
		'+'
			'a'
			'1'

alan@alan-PC:~/asquel$ 
```

## En esta versión:

* Sintaxis creada
* Correcciones menores al simobolizador
* Modelo de procesamiento establecido, de mayor nivel hacia abajo.


## Descarga
### Última versión estable:
[Asquel 0.1.13](https://sourceforge.net/projects/asquel-old/files/asquel-0.1.3.zip/download) es la mejor versión de asquel, es anterior al cambio de modelo y tiene todas las caracteristicas que se habían conseguido como el modo interactivo, analisis de archivos, gestor de errores entre otros.
### Versión actual:
- Puedes clonar este repositorio con `git clone git://github.com/SoyZatarain/asquel.git`
- Tambien puedes dar clic [aquí](https://github.com/SoyZatarain/asquel/archive/master.zip) para descargar el paquete a través del navegador.
### Versiones anteriores:
Puedes descargar desde la versión 0.0, 0.1, etc. de [esta lista](https://sourceforge.net/projects/asquel-old/files/) alojada por SourceForge.

## Desarrollo futuro

* Crear evaluador de expresiones
* Crear funciones estándar como print(), por ejemplo <- __parcialmente implementado__
* Crear estructura de flujo

## Licencia

La licencia que cubre a Asquel está en doc/LICENSE o en [este enlace](https://raw.githubusercontent.com/SoyZatarain/asquel/master/doc/LICENSE).

---

> [Alan Zatarain](https://soyzatarain.github.io/) &nbsp;&middot;&nbsp;
> [Facebook](https://www.facebook.com/SoyZatarain/) &nbsp;&middot;&nbsp;
> Twitter [@SoyZatarain](https://twitter.com/SoyZatarain)

