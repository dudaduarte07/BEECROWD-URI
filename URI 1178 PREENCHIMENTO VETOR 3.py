#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = float(input())
contador = 0
while contador < 100:
    print('N[%d] = %.4f' % (contador, n))
    contador = contador + 1
    n = n / 2