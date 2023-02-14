#!/usr/bin/env python3
# -*- coding: utf-8 -*-

valor = input().split()
a = int(valor[0])
ultimo = len(valor)
n = int(valor[ultimo - 1])

soma = 0
for i in range(0, n):
    soma = soma + a + i
print(soma)
