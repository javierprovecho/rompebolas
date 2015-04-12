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

class Tablero:
 
    def __init__(self):
        self.cuadricula = [[0 for i in range(9)] for j in range(9)]
        self.puntuacion = 0
        self.multiplicador = 0
        
    def romper(self, x, y):
        color = self.cuadricula[x][y]
        
        if x < len(self.cuadricula) - 1:
            if self.cuadricula[x + 1][y] == color:
                self.cuadricula[x][y] = 0
                self.multiplicador = self.multiplicador + 1
                self.romper(x + 1, y)
        if x > 0:
            if self.cuadricula[x - 1][y] == color:
                self.cuadricula[x][y] = 0
                self.multiplicador = self.multiplicador + 1
                self.romper(x - 1, y)
        if y < len(self.cuadricula[0]) - 1:
            if self.cuadricula[x][y + 1] == color:
                self.cuadricula[x][y] = 0
                self.multiplicador = self.multiplicador + 1
                self.romper(x, y + 1)
        if y > 0:
            if self.cuadricula[x][y - 1] == color:
                self.cuadricula[x][y] = 0
                self.multiplicador = self.multiplicador + 1
                self.romper(x, y - 1)
        if self.multiplicador > 1:
            self.cuadricula[x][y] = 0
                
    def mover(self, x, y):
        self.multiplicador = 1
        self.romper(x-1, y-1)
        if self.multiplicador > 1:
            self.puntuacion = self.puntuacion + (self.multiplicador * 5)
            
    def limpiar(self):
        for c in reversed(range(9)):
            for f in reversed(range(8)):
                if self.cuadricula[f][c] == 0:
                    for k in range(f + 1, 9):
                        self.cuadricula[k - 1][c] = self.cuadricula[k][c]
                    self.cuadricula[8][c] = 0
        
        for c in reversed(range(9)):
            columna_vacia = True
            for f in reversed(range(9)):
                if self.cuadricula[f][c] != 0:
                    columna_vacia = False
                    break
            if columna_vacia:
                for f in reversed(range(9)):
                    del self.cuadricula[f][c]
                    self.cuadricula[f].append(0)
    
    def vacio(self):
        for f in range(9):
            for c in range(9):
                if self.cuadricula[f][c] !=  0:
                    return False
        return True
                    