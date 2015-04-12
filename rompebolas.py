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
from random import randint

def jugar():
    tablero = menu_principal()
    mostrar_tablero(tablero, tablero.puntuacion, -1)
    while True:
        tablero.mover(
            int(raw_input("Introduzca la fila deseada:")),
            int(raw_input("Introduzca la columna deseada:"))
        )
        tablero.limpiar()
        mostrar_tablero(tablero, tablero.puntuacion, -1)
        if tablero.vacio():
            print "Partida terminada con", tablero.puntuacion, "puntos."
            break
    
def menu_principal():
    while True:
        print\
            "Elija tipo de tablero u otras opciones\n",\
            "\t1. Fácil\n",\
            "\t2. Intermedio\n",\
            "\t3. Difícil\n",\
            "\t4. Tablero fijo\n",\
            "\t5. Mejores puntuaciones\n",\
            "\t6. Borrar mejores puntuaciones\n",\
            "\t0. Salir\n"
        try:
            opcion = int(raw_input())
            if opcion <= 6 and opcion >= 0:
                break
            else:
                raise
        except:
            print "Error: Seleccione una opcion válida"
    
    tablero = Tablero()
    if opcion == 1:
        tablero_facil(tablero)
    elif opcion == 2:
        tablero_intermedio(tablero)
    elif opcion == 3:
        tablero_dificil(tablero)
    elif opcion == 0:
        exit()
        
    return tablero
    
    
def tablero_facil(tablero):
    for f in range(9):
        for c in range(9):
            tablero.cuadricula[f][c] = randint(1, 3)
            
def tablero_intermedio(tablero):
    for f in range(9):
        for c in range(9):
            tablero.cuadricula[f][c] = randint(1, 4)
            
def tablero_dificil(tablero):
    for f in range(9):
        for c in range(9):
            tablero.cuadricula[f][c] = randint(1, 5)
    
def mostrar_tablero(tablero, puntuacion_actual, puntuacion_maxima):
    print \
        "\033[4m ",\
        "|",\
        " ".join(str(c) for c in range(1, 10)),\
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
    for f in reversed(range(1, 10)):
        lineas += 1
        extra = marcador(puntuacion_actual, puntuacion_maxima, lineas)
        
        print \
            str(f),\
            "|",\
            " ".join(str(tablero.cuadricula[f-1][c-1]\
                if tablero.cuadricula[f-1][c-1] > 0 else " "\
            )\
                for c in range(1, 10)),\
            "".join(extra)

if __name__ == "__main__":
    jugar()