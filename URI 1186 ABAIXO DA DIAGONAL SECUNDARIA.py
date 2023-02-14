#!/usr/bin/env python3
# -*- coding: utf-8 -*-

op = input()
A = []

for i in range(12):
    A.append([])
    for j in range(12):
        num = float(input())
        A[i].append(num)

soma = 0
contador = 0
x = 0
y = 11
for i in range (y, 0, -1):
    x = x + 1
    for j in range (x, 12):
        soma = soma + A[i][j]
        contador = contador + 1

if op == 'S':
    print(soma)
if op == 'M':
    media = soma / contador
    print('%.1f' % media)
