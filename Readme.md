
<h1 align="center">
  <br>
  <a href="https://asquelito.tumblr.com/"><img src="https://raw.githubusercontent.com/SoyZatarain/asquel/master/icono.png" alt="Asquelito" width="200"></a>
  <br>
  Asquel 0.1.13
  <br>
</h1>

<h4 align="center">Lenguaje de programación extremadamente fácil para introducir conceptos básicos en clases universitarias.</h4>

<p align="center">
  <a href="https://asquelito.tumblr.com/">
    <img src="https://img.shields.io/badge/Estado-En%20pruebas-yellow.svg">
  </a>
  <a href="https://asquelito.tumblr.com/"><img src="https://img.shields.io/badge/Versi%C3%B3n-0.1.13-green.svg"></a>
</p>
<br>

![screenshot](https://raw.githubusercontent.com/SoyZatarain/asquel/master/Captura%20de%20pantalla%20de%202017-09-03%2006-47-14.png)

## En esta versión...

Cabe mencionar que el lenguaje aún no está del todo construido, por lo que carece de sintaxis. Por ahora lo que se incluye en el paquete es la muestra de como funciona su analizador de expresiones. Asquel se compondrá enteramente de expresiones matemáticas, por lo que este analizador debe ser perfecto.

* Las expresiones pueden tener la extensión y contenido que se desee
* Capaz de procesar sumas, restas, multiplicaciones y divisiones
* Actua según la jerarquía de resolución, asignando prioridades a cada operación y dividiendola en su forma más simple
* Capacidad para incluir parentesis, estableciendo jerarquía personalizada
* Código fácil de leer
* Operciones con numeros negativos
* El resultado se dará siempre con tantos decimales como haya disponibles
* Facilmente modificable
* Compatibel con Linux, BSD, Windows y MacOS ejecutando Python 2.x y Python 3.x

## ¿Cómo se ejecuta?

###En POSIX (Linux, BSD, macOS):
Localiza la carpeta raíz, donde se encuentra el documeto asquel.py, abre una terminal y ejecuta: `./asquel.py`, si arroja error ejecuta `python asquel.py`

###En Windows:
Localiza la carpeta raíz, donde se encuentra el documento asquel.py y dale doble clic.

###Sesión de jemplo:
Aquí se muestra un ejemplo de sesión con Asquel resolviendo operaciones sencillas y una expresión compleja, finalmente un error de denotación.
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

## Descarga

- Puedes clonar este repositorio con `git clone git://github.com/SoyZatarain/asquel.git`
- Tambien puedes dar clic [aquí](https://github.com/SoyZatarain/asquel/archive/master.zip) para descargar el paquete a través del navegador.

## Desarrollo futuro

La sintaxis será creada pronto, he estado haciendo pruebas y creo tener el abstracto listo, sólo me falta trasladarlo a código. Un dato importante es que no aseguro alguna fecha para que salga una versión "1.0", ya que liberaré Asquel sólo cuando esté listo. Espero que más gente se sume y empiece a hacer aportaciones, sino es en código, al menos haciendo pruebas y reportando bugs.

#### License

La licencia que cubre a Asquel está en doc/LICENSE o en [este enlace](https://raw.githubusercontent.com/SoyZatarain/asquel/master/doc/LICENSE).

---

> [Alan Zatarain](https://soyzatarain.github.io/) &nbsp;&middot;&nbsp;
> [Facebook](https://www.facebook.com/SoyZatarain/) &nbsp;&middot;&nbsp;
> Twitter [@SoyZatarain](https://twitter.com/SoyZatarain)
