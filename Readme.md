
<h1 align="center">
  <br>
  <a href="https://asquelito.tumblr.com/"><img src="https://raw.githubusercontent.com/SoyZatarain/asquel/master/icono.png" alt="Asquelito" width="200"></a>
  <br>
  Asquel 0.2b
  <br>
</h1>

<h4 align="center">Lenguaje de programación extremadamente fácil para introducir conceptos básicos en clases universitarias.</h4>

<p align="center">
  <a href="https://asquelito.tumblr.com/">
    <img src="https://img.shields.io/badge/Estado-Estable-green.svg">
  </a>
  <a href="https://asquelito.tumblr.com/"><img src="https://img.shields.io/badge/Versi%C3%B3n-0.2b-green.svg"></a>
</p>
<br>

## ¿Qué es Asquel?
Es un lenguaje de programación muy sencillo, con una sintaxis simple y de manejo fácil de aprender a través de una línea de comandos. EStá pensado para servir como primer lenguaje de programación para estudiantes universitarios que recurren a lenguajes más complejos como Java o C# para aprender, lo que resulta contra producente, ya que normalmente en los 6 meses que dura el curso de introducción a la programación no aprenden los conceptos básicos y después tienen problemas en clases superiores, o ya directamente reprueban.
Asquel aún no está terminado, y la sintaxis aún se está diseñando, no persigue el propósito de equipararse a Python o Perl, por ejemplo, sino que apuesta por ser fácil de aprender en menos de un mes y ser el primer escalón de los estudiantes, por eso su sintaxis debe ser minimizada, compacta y fácil de leer.
Asquel está implementado en Python, pero al diseñar la sintaxis por completo se trasladará a C++.

## Modo de uso

Asquel tiene dos modos de uso, el interactivo y el interprete de archivos:

### Modo interactivo
Para acceder al modo interactivo, localizamos la carpeta raíz del proyecto, donde se encuentra el doicumento "asquel.py", abrir una terminal o simbolo del sistema ahí y ejecutar `[python o python3] asquel.py`.
Tiene el bucle fetch-decode-execute, por lo que al ejecutarse, se comporta como una consola de comandos o simbolo de sistema, donde se pueden introducir ordenes para ser inmediatamente ejecutadas. Por ahora Asquel sólo acepta expresiones matemáticas (como las que meterías a una calculadora), por lo que una sesión en modo interactivo se ve algo así:
```bash
Copyright (c)2017 Alan Ramirez Zatarain
https://github.com/SoyZatarain/asquel/blob/master/doc/LICENSE

Asquelito:~$ 1+5
 6 

Asquelito:~$ 4-8
 -4 

Asquelito:~$ 8*7
 56 

Asquelito:~$ 9/7
 1.2857142857142858 

Asquelito:~$ (78/25)-(56/78)
 2.402051282051282 

Asquelito:~$ (56/7*8-9
 Error: La expresión está mal denotada.

Asquelito:~$

```

### Modo interprete de archivos:
Podemos cargar un archivo para que asquel lo interprete directamente en vez de introducir las expresiones de una en una, podemos hacer un archivo que las contenga, de a una por cada línea, se puede consultar el directorio "ejemplos" que contiene una muestra de como se hace esto (aunque no es nada complicado, es intuitivo).

La estructura del comando para cargar el archivo a ser interpretado es:
`[python o python3] [-d] asquel.py <archivo>`

Tal como se muestra, se puede usar el interprete python 2.x o python 3.x, pero se recomienda m[as [este [ultimo, ya que en python 2.x los decimales se cortan. Luego tenemos el modificador -d que es opcional y de ser usado, vacía los datos con su tipo asignado en forma de lista ordenada. el archivo ejecutable es asquel.py, es el que hace todo el trabajo junto con sus módulos internos. Finalemente, el último elemento de la línea es el archivo que vas a ingresar al interprete, por ejemplo "archivo.txt" que se incluye en la carpeta "ejemplos":
```
alan@alan-PC:~/asquel$ python3 asquel.py prueba.txt
Copyright (c)2017 Alan Ramirez Zatarain
https://github.com/SoyZatarain/asquel/blob/master/doc/LICENSE

1 29
2 31
3 39.0
4 552
Error en linea 5
6 9.419128386336867
7 -6318.004273504273

alan@alan-PC:~/asquel$
```

## En esta versión:

* Las expresiones pueden tener la extensión y contenido que se desee
* Capaz de procesar sumas, restas, multiplicaciones y divisiones
* Actua según la jerarquía de resolución, asignando prioridades a cada operación y dividiendola en su forma más simple
* Capacidad para incluir parentesis, estableciendo jerarquía personalizada
* Código fácil de leer
* Operciones con numeros negativos
* El resultado se dará siempre con tantos decimales como haya disponibles
* Facilmente modificable
* Compatibel con Linux, BSD, Windows y MacOS ejecutando Python 2.x y Python 3.x


## Descarga
### Versión actual:
- Puedes clonar este repositorio con `git clone git://github.com/SoyZatarain/asquel.git`
- Tambien puedes dar clic [aquí](https://github.com/SoyZatarain/asquel/archive/master.zip) para descargar el paquete a través del navegador.
### Versiones anteriores:
Puedes descargar desde la versión 0.0, 0.1, etc. de [esta lista](https://sourceforge.net/projects/asquel-old/files/) alojada por SourceForge.

## Desarrollo futuro

La sintaxis será creada pronto, he estado haciendo pruebas y creo tener el abstracto listo, sólo me falta trasladarlo a código. Un dato importante es que no aseguro alguna fecha para que salga una versión "1.0", ya que liberaré Asquel sólo cuando esté listo. Espero que más gente se sume y empiece a hacer aportaciones, sino es en código, al menos haciendo pruebas y reportando bugs.

## Licencia

La licencia que cubre a Asquel está en doc/LICENSE o en [este enlace](https://raw.githubusercontent.com/SoyZatarain/asquel/master/doc/LICENSE).

---

> [Alan Zatarain](https://soyzatarain.github.io/) &nbsp;&middot;&nbsp;
> [Facebook](https://www.facebook.com/SoyZatarain/) &nbsp;&middot;&nbsp;
> Twitter [@SoyZatarain](https://twitter.com/SoyZatarain)
