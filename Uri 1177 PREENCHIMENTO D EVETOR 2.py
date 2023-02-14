#!/usr/bin/env python3
# -*- coding: utf-8 -*-

t = int(input())
x = 0
n = 0
contador = 0
while contador < 1000:
    while n < t:
        print('N[%d] = %d' % (x, n))
        contador = contador + 1
        n = n + 1
        x = x + 1
        if contador == 1000:
            exit(0)
    if n == t:
        n = 0
    

