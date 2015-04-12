#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# The MIT License (MIT)
# 
# Copyright (c) 2015 Javier Provecho Fernandez
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from tablero import Tablero
def main():
    tablero = Tablero()
    mostrar_tablero(tablero, 0, 1)
    
def mostrar_tablero(tablero, puntuacion_actual, puntuacion_maxima):
    print \
        "\033[4m ",\
        "|",\
        " ".join(str(i) for i in range(1, len(tablero.cuadricula[0]) + 1)),\
        "\033[0m",\
        "\t \033[4mpuntos\033[0m"
    
    def marcador(puntuacion_actual, puntuacion_maxima, lineas):
        extra = ""
        if lineas is 1:
            extra = "\t\t", str(puntuacion_actual)
        elif lineas is 3:
            extra = "\t \033[4mmáximo\033[0m"
        elif lineas is 4:
            extra = "\t\t", str(puntuacion_maxima)
        return extra
            
    lineas = 0
    for i in reversed(range(1, len(tablero.cuadricula) + 1)):
        lineas += 1
        extra = marcador(puntuacion_actual, puntuacion_maxima, lineas)
        
        print \
            str(i),\
            "|",\
            " ".join(str(tablero.cuadricula[i-1][j-1])\
                for j in range(1, len(tablero.cuadricula[0]) + 1)),\
            "".join(extra)


main()