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
import json

def jugar():
    tablero = menu_principal()
    while True:
        mostrar_tablero(tablero, tablero.puntuacion, -1)
        while True:
            try:
                f, c =\
                    int(raw_input("Introduzca la fila deseada: ")),\
                    int(raw_input("Introduzca la columna deseada: "))
                if f <= 9 and f >= 1 and c <= 9 and c >= 1:
                    tablero.mover(f, c)
                    tablero.limpiar()
                    mostrar_tablero(tablero, tablero.puntuacion, -1)
                    if tablero.vacio():
                        print "Partida terminada con", tablero.puntuacion, "puntos."
                        anadir_puntuacion(tablero.tipo_partida, tablero.puntuacion)
                        break
                elif f == 0 and c == 0:
                    break
                else:
                    raise
            except:
                print "Error: Seleccione una posición válida"
        while True:
            print\
                "Elija una opción\n",\
                "\t1. Jugar de nuevo\n",\
                "\t0. Volver al menú principal\n"
            try:
                opcion = int(raw_input())
                if opcion <= 1 and opcion >= 0:
                    break
                else:
                    raise
            except:
                print "Error: Seleccione una opcion válida"
        if opcion == 1:
            tablero.puntuacion = 0
            if tablero.tipo_partida == 1:
                tablero_facil(tablero)
            elif tablero.tipo_partida == 2:
                tablero_intermedio(tablero)
            elif tablero.tipo_partida == 3:
                tablero_dificil(tablero)
            elif tablero.tipo_partida == 41:
                tablero_cuadrado_tres_colores(tablero)
            elif tablero.tipo_partida == 42:
                tablero_rombo_cuatro_colores(tablero)
            elif tablero.tipo_partida == 43:
                tablero_casi_damero_dos_colores(tablero)
        elif opcion == 0:
            anadir_puntuacion(tablero.tipo_partida, tablero.puntuacion)
            print "Partida terminada con", tablero.puntuacion, "puntos."
            tablero = menu_principal()
    
def menu_principal():
    while True:
        while True:
            print\
                "Elija tipo de tablero u otras opciones\n",\
                "\t1. Fácil\n",\
                "\t2. Intermedio\n",\
                "\t3. Difícil\n",\
                "\t4. Tablero fijo\n",\
                "\t5. Mejores puntuaciones (no implementado)\n",\
                "\t6. Borrar mejores puntuaciones (no implementado)\n",\
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
            tablero.tipo_partida = 1
            break
        elif opcion == 2:
            tablero_intermedio(tablero)
            tablero.tipo_partida = 2
            break
        elif opcion == 3:
            tablero_dificil(tablero)
            tablero.tipo_partida = 3
            break
        elif opcion == 4:
            menu_secundario(tablero)
            if tablero is not None:
                break
        elif opcion == 5:
            mejores_puntuaciones()
        elif opcion == 6:
            borrar_mejores_puntuaciones()
        elif opcion == 0:
            exit()
        
    return tablero

def menu_secundario(tablero):
    while True:
        print\
            "Elija un tablero fijo\n",\
            "\t1. Cuadrado con tres colores\n",\
            "\t2. Rombo con 4 colores\n",\
            "\t3. Casi-damero, con dos colores\n",\
            "\t0. Volver (no implementado)\n"
        try:
            opcion = int(raw_input())
            if opcion <= 3 and opcion >= 1:
                break
            else:
                raise
        except:
            print "Error: Seleccione una opcion válida"
    
    if opcion == 1:
        tablero_cuadrado_tres_colores(tablero)
        tablero.tipo_partida = 41
    elif opcion == 2:
        tablero_rombo_cuatro_colores(tablero)
        tablero.tipo_partida = 42
    elif opcion == 3:
        tablero_casi_damero_dos_colores(tablero)
        tablero.tipo_partida = 43
    
def mejores_puntuaciones():
    try:
        f = open("puntuaciones.json")
        puntuaciones = json.loads(f.read())
        f.close()
        print\
            "Mejores puntuaciones\n",\
            "\t1. Tablero fácil :\t\t", str(puntuaciones.get("1")), "\n",\
            "\t2. Tablero intermedio :\t\t", str(puntuaciones.get("2")), "\n",\
            "\t3. Tablero difícil :\t\t", str(puntuaciones.get("3")), "\n",\
            "\t4. Tablero fijo cuadrado :\t", str(puntuaciones.get("41")), "\n",\
            "\t5. Tablero fijo rombo :\t\t", str(puntuaciones.get("42")), "\n",\
            "\t6. Tablero fijo damero :\t", str(puntuaciones.get("43")), "\n"
    except:
        print "No hay puntuaciones previas"

def borrar_mejores_puntuaciones():
    puntuaciones = {
        1:  0,
        2:  0,
        3:  0,
        41: 0,
        42: 0,
        43: 0
    }
    f = open("puntuaciones.json", "w")
    f.write(json.dumps(puntuaciones))
    f.close()

def anadir_puntuacion(tipo_partida, puntuacion):
    try:
        f = open("puntuaciones.json")
        puntuaciones = json.loads(f.read())
        f.close()
        if puntuaciones.get(str(tipo_partida)) < puntuacion:
            puntuaciones[str(tipo_partida)] = puntuacion
            f = open("puntuaciones.json", "w")
            f.write(json.dumps(puntuaciones))
            f.close()
    except:
        puntuaciones = {
            1:  0,
            2:  0,
            3:  0,
            41: 0,
            42: 0,
            43: 0
        }
        puntuaciones[str(tipo_partida)] = puntuacion
        f = open("puntuaciones.json", "w")
        f.write(json.dumps(puntuaciones))
        f.close()

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
            
def tablero_cuadrado_tres_colores(tablero):
    tablero.cuadricula = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 2, 3, 3, 3, 3, 3, 2, 1],
        [1, 2, 3, 1, 1, 1, 3, 2, 1],
        [1, 2, 3, 1, 2, 1, 3, 2, 1],
        [1, 2, 3, 1, 1, 1, 3, 2, 1],
        [1, 2, 3, 3, 3, 3, 3, 2, 1],
        [1, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    
def tablero_rombo_cuatro_colores(tablero):
    tablero.cuadricula = [
        [4, 4, 4, 4, 1, 4, 4, 4, 4],
        [4, 4, 4, 1, 2, 1, 4, 4, 4],
        [4, 4, 1, 2, 3, 2, 1, 4, 4],
        [4, 1, 2, 3, 1, 3, 2, 1, 4],
        [1, 2, 3, 1, 2, 1, 3, 2, 1],
        [4, 1, 2, 3, 1, 3, 2, 1, 4],
        [4, 4, 1, 2, 3, 2, 1, 4, 4],
        [4, 4, 4, 1, 2, 1, 4, 4, 4],
        [4, 4, 4, 4, 1, 4, 4, 4, 4],
    ]
    
def tablero_casi_damero_dos_colores(tablero):
    tablero.cuadricula = [
        [1, 2, 1, 2, 1, 2, 1, 2, 1],
        [2, 1, 2, 1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1, 2, 1],
        [2, 1, 2, 1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1, 2, 1],
        [2, 1, 2, 1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1, 2, 1],
        [2, 1, 2, 1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1, 2, 1],
    ]
    f = randint(0, 8)
    c = randint(0, 8)
    if tablero.cuadricula[f][c] == 1:
        tablero.cuadricula[f][c] = 2
    else:
        tablero.cuadricula[f][c] = 1
    
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
