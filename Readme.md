<h1 align="center">
  <br>
  <a href="https://asquelito.tumblr.com/"><img src="brand.png" alt="Asquelito"></a>
  <br>
  Lenguaje Asquel
  <br>
</h1>

<h4 align="center">Lenguaje de programación extremadamente fácil para introducir conceptos básicos en clases universitarias.</h4>

<p align="center">
  <a href="https://asquelito.tumblr.com/">
    <img src="https://img.shields.io/badge/Estado-Estable-green.svg">
  </a>
  <a href="https://asquelito.tumblr.com/"><img src="https://img.shields.io/badge/Versi%C3%B3n-1.0-green.svg"></a>
</p>
<br>
**Asquel** es materal didáctico para clases de fundamentos de programación en forma de un lenguaje de programación sencillo orientado a matemáticas, pensado para ser el primer escalón entre la teoría y un lenguaje de programación listo para producción.

Asquel está implementado en Python, compilado a un ejecutable mediante la aplicación [Nuitka](http://nuitka.net/), por lo que de no existir una distribución binaria para el sistema en el que necesitas ejecutarlo, puedes usarlo en su forma de código fuente con el interprete de Python 3.x.

La sintaxis extremadamente sencilla de Asquel permiten ser aprendido en un máximo de un mes, y establece elementos comunes de lenguajes populares para que los alumnos se familiarizen con tales conceptos.

Tu primer programa en Asquel
------------------------
Siendo un lenguaje orientado a matemáticas, no hay manejo de tipos char o string en Asquel, en su lugar, sólo trabajamos con valores numericos. El siguiente es un ejemplo incluido en el archivo `ejemplos/prueba.asq`.

```
a = 1 + 1 * 8 - 9 / 6 / 17;
b = 7;
a = a + b;
imprimir(a + 1);
```

Al ejecutarlo, se verá algo así:

```
alan@alan-PC:~$ asquel prueba.asq
16.911764705882355

alan@alan-PC:~$ 
```

Sintaxis
------------------------
La sintaxis es tan sencilla como esto:

* Las variables sólo se pueden simbolizar con una letra o una palabra, por ejemplo, a la variable `a` le asignaremos el valor de 1 y a `var` le asignamos valor de 2 de la siguente forma:
```
Esto está bien:
a = 1;
var = 2;
```

* Todos los valores deben ser numericos, eneros (integer) o decimales (float):
```
Esto está bien:
a = 1;

Esto está mal y arrojará error:
a = "Hola";
```

* Se puede asignar una expresión a una variable, lo que devolverá será el resultado de evaluar y resolver la expresión respetando jerarquía de resolución:
```
Ejemplo:
a = 1 / 2 * 3 - 7 / 8 * 7;

También se pueden incluir variables predefinidas en la expresión:
a = 1 + 5;
b = 19 - a;
```

* Las variables se pueden reasignar a si mismas:
```
Ejemplo:
a = 19 * 7;
a = a + 2;
```

* Siempre deben usarse separadores, en el caso de Asquel se usa el punto y coma (;):
```
Esto está bien:
a = 1;
b = 19 * a;
c = 14 / 45 * 78 - 65 + 78 * 87 / 78 + b;
d = 192 / 168 * b - 254;

Esto está mal y arrojará error:
a = 1
b = 19 * a
c = 14 / 45 * 78 - 65 + 78 * 87 / 78 + b
d = 192 / 168 * b - 254
```

* La función imprimir() es el único elemento de Asquel que puede interactuar con la salida estándar (la terminal en Linux o simbolo del sistema en Windows), y se puede usar de las siguientes formas:
```
Para imprimir una variable:
a = 1;
b = 19 * a;
c = 14 / 45 * 78 - 65 + 78 * 87 / 78 + b;
d = 192 / 168 * b - 254;
imprimir(d);

Para imprimir un número:
imprimir(12);

Para imprimir el resultado de una expresión:
imprimir(13 / 24 * 24 - 35 + 345);

Para imprimir una expresión incluida una variable:
a = 13 / 24 * 34 - 35 + 24;
imprimir(134 / 687 * 12 / 467 + 35 - a * 24 / 24 * 1);
```

* La expresiones pueden contener parentesis, sumas, restas, multiplicaciones y divisiones:
```
a = 123 / (23 * 34) * 35456 - (131243 +2353655) / (75 - 2)
```

* Para ejecutar alguno de estos programas de ejemplo, debes guardarlos en un archivo de texto plano con extensión .ASQ obligatoriamente o Asquel no lo cargará. También puedes usar el archivo de ejemplo que se incluye en la carpeta `ejemplos/`.
Una vez que tienes tu archivo listo para ser ejecutado, y haz instalado Asquel, puedes ejecutar tus programas con una línea tan simple como esta:
```
asquel archivo.asq
```

Opciones de línea de comandos
------------------------
```
alan@alan-PC:~$ asquel
Asquel interpreter 1.0
Copyright 2017 Alan Ramirez Zatarain
https://raw.githubusercontent.com/SoyZatarain/asquel/master/doc/LICENSE

Uso: python3 asquel.py [opcion] <archivo.asq>

  Opciones:
  -d, --diccionario      Muestra asignaci[on de tipo a los simbolos
  -a, --arbol            Muestra arbol de sintaxis abstracta
```

Descargar
------------------------
| Sistema Operativo | Arquitectura | Archivo |
| ------------------------ | ---------------- | ---------- |
| Windows | x86 | asquel-1.0-winx86.zip |
| Windows | x64 | asquel-1.0-winx64.zip |
| GNU/Linux | x86 | asquel-1.0-linuxx86.tar.gz |
| GNU/Linux | x64 | asquel-1.0-linuxx64.tar.gz |
| FreeBSD | x86 | asquel-1.0-freebsdx86.tbz |
| FreeBSD | x64 | asquel-1.0-freebsdx64.tbz |

** Nota: Aunque existen estas distribuciones binarias, siempre se recomienda mejor construirlo desde código fuente ** (Más abajo se explica cómo).

Construir desde código fuente
------------------------
Puedes obtener el código fuente de las siguientes formas:

* Descarga [aquí](https://github.com/SoyZatarain/asquel/archive/master.zip) un paquete comprimido a través del navegador.
* Clona este reporitorio con `git clone git://github.com/SoyZatarain/asquel.git`.
             
#### En GNU/Linux, BSD y macOS

Asegurate de tener instalados [Python 3.x](https://www.python.org/downloads/) y [Nuitka](http://nuitka.net/pages/download.html).
La rutina es sencilla, los pasos de construcción de toda la vida:
1. En la carpeta raíz del proyecto (donde se encuentra asquel.py) ejecuta`chmod +x configure`
2. Ejecuta `./configure`
3. Se generará un Makefile, ejecuta `make`
4. Cuando termine de compilar, ejecuta `make install`

También incluye la opción `make clean` para limpiar el proyecto y `make remove` para desinstalar asquel de tu sistema.

#### En Windows
Asegurate de tener instalados [Python 3.x](https://www.python.org/downloads/) y [Nuitka](http://nuitka.net/pages/download.html).
Da doble clic a `build.bat` y luego como administrador en el simbolo del sistema ejecutas `install.bat`. Tambien se incluyen `clean.bat` para limpiar el proyecto y `remove.bat` para desinstalarlo de tu sistema.

Ejecutar desde código fuente
------------------------
Debido a que Asquel está escrito en Python, puede ser ejecutado directamente sin tener que compilarse. Para esto puedes usarlo de la siguiente forma en cualquier sistema operativo que pueda ejecutar Python 3.x:
```
python asquel.py archivo.asq
```
Nótese que en sistemas POSIX se diferencía a Python 2.x y 3.x a través del nombre de su ejecutable, por lo que probablemente deba ser `python3` en vez de `python`.

Contribuir
-------------------------
Me sentiré muy feliz si encuentras a Asquel útil para tus proyectos personales, educativos, experimentales o simplemente por curiosidad, ya que se puede rescatar mucho de él, como el evaluador de expresiones, el procesador de simbolos, el evaluador, etc.
Si deseas contribuir con código que dotaría a Asquel de nuevas características puedes hacerlo libremente creando un pull request, o sometiendo tus cambios directamente a revisión a través de mis vías de contacto disponibles en [mi sitio de github](https://soyzatarain.github.com/) o aquí más abajo.
Te invito a que hagas un fork de Asquel y lo mejores según tus necesidades, si sientes que tienes una mejor idea y por tanto tu desarrollo debe apartarse de la línea original, tienes mi bendición y licencia para hacerlo. No estas obligado a avisarme, pero si pudieras, me encantaría saber en qué te ayudó Asquel.

Soporte
-------------------------
Si deseas discutir algún aspecto de Asquel directamente conmigo o tienes alguna duda, puedes consultarme mediante las redes sociales descritas hasta el fondo de este documento.

## Licencia

La licencia que cubre a Asquel está en doc/LICENSE o en [este enlace](https://raw.githubusercontent.com/SoyZatarain/asquel/master/doc/LICENSE).

---

> [Alan Zatarain](https://soyzatarain.github.io/) &nbsp;&middot;&nbsp;
> [Facebook](https://www.facebook.com/SoyZatarain/) &nbsp;&middot;&nbsp;
> Twitter [@SoyZatarain](https://twitter.com/SoyZatarain)

