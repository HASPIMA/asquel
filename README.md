# [Asquel](http://asquel.hol.es/)
##### Mathematical programming language

[![Selenium Test Status](https://saucelabs.com/browser-matrix/bootstrap.svg)](http://www.asquel.hol.es/tests) [![Build Status](https://img.shields.io/travis/twbs/bootstrap/v4-dev.svg)](http://www.asquel.hol.es/build-status)

Asquel is a new programming language deigned by the mexican Industrial Engineering student [Alan Ramirez Zatarain](http://zatarain.co.nf), to be easy to understand and use, and with a mathematical syntax, to solve problems of career clases.

The labs that work on Asquel are named "Asquel holes" and you can consult a list of them in <http://asquel.hol.es>!

## Table of contents

- [Quick start](#quick-start)
- [Bugs and feature requests](#bugs-and-feature-requests)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Community](#community)
- [Versioning](#versioning)
- [Holes](#holes)
- [Copyright and license](#copyright-and-license)

## Quick start

In order to download binary releases of asquel you can do it from the [asquel holes' official latest release](http://asquel.hol.es/latest.zip) direct download.

To get the sources you can:

- Clone this repo: `git clone https://github.com/SoyZatarain/asquel.git`
- Download the [compressed archive](http://asquel.hol.es/latest-src.tar.gz).

To learn the syntax you can read the reference guide included in both archives. The interpreter is written in Python, so it does not need to be installed, you just need to run a terminal in the folder in wich the interpreter is located and do `python asquel.pyc`

### What is asquel conformed of?

This diagram represents the main idea for the interpeter and what parts of it i have already written:

```
Asquel
├── Parser
│   ├── Lexical analisis routine
│   ├── Trim expresion into the minimum posible unit
│   ├── Realize the operations in priority system
│   └── Send result to output
└── Interface
    ├── Read expresion
    └── Show result
```

We will have to develop our own parser and functions library to make asquel independent of python.


## Bugs and feature requests

Do you have a great idea and you want it to be part of asquel? First you should read if someone else already had the same idea as seen in our TODO file. If you had an original idea and you already have the code, you can commit your changes into a new branch. If your idea is not in our plans yet, [please submit it to our discuss forum](https://asquelito.tumblr.com/).


## Documentation

Every single release of asquel has and will always have its manual, reference guide and examples in the distribution package, so it will be in every version you get.

### I only want docs, not the package

You can get them in the [asquel holes library](http://www.asquel.hol.es/docs/).



## Contributing

There are many ways to contribute to our project for example:

- Donation
- Suggesting ideas
- Asking for new features
- Fixing bugs
- Porting asquel to other plattforms
- Putting your code in asquel
- Create new branches for new implementations of this language

You can get more information in our [discussion forum](https://asquelito.tumblr.com/) or in the [official home of asquel](http://www.asquel.hol.es/).



## Community

Get updates on asquel's development

- Join the [official discussion forum](https://asquelito.tumblr.com/).
- Read the [Asquel holes blog](http://www.asquel.hol.es/blog).
- Follow Alan Zatarain on his [facebook page](https://www.facebook.com/SoyZatarain/).



## Versioning

I will thank you a lot if you find Asquel useful to your own project, if you want to implement some new feature that helps you to the interpreter, trust me, that feature will help to much more people with your same curiousity. If you add your code to Asquel and you feel it is time to get appart of the main developement to envolve by your own, feel free to create your own version of Asquel.

If you can make an upgrade to the code or to some specific function or routine, you can do it, and let me know if you want me to release an improved version with your upgrade.


## Holes

**UACJ**

If you are a student of Universidad Autónoma de Ciudad Juárez, of any career or intitute, you can be part of the physic core developement team just sending me a message with your intention and i will send you the developement and discussion sessions schedule, so you can asist to our gatherings.

**Juarez local asquel hole**

This is more a plan of extension than a real asquel hole. No matter what university you are in, even if you are not at any university. Everyone can join the local asquel hole of Juarez. If you want this project to go on, contact me on my [facebook page](https://www.facebook.com/SoyZatarain/), and we will make an appointment.


## Copyright and license

Asquel documentation and object and source code copyright 2017 [Alan Ramirez Zatarain](http://zatarain.co.nf). Code released under [our own license](http://asquel.hol.es/LICENSE).

