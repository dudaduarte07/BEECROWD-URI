#!/usr/bin/env python3
# -*- coding: utf-8 -*-

loop = True

while loop == True:
    n = int(input())

    if n == 0:
        loop = False
        exit(0)

    lista = []
    for i in range (n):
        lista2 = []
        for j in range(n):
            lista2.append(1)
        lista.append(lista2)

    valor = 1
    superior = 0
    lateral_esquerda = 0
    inferior = n - 1
    lateral_direita = n - 1

    if n % 2 == 0:
        meio = n // 2
    else:
        meio = (n + 1) // 2

    while valor <= meio:
        i = lateral_esquerda
        while i <= lateral_direita:
            lista[superior][i] = valor
            lista[inferior][i] = valor
            i = i + 1
        
        i = superior + 1
        while i < inferior:
            lista[i][lateral_esquerda] = valor
            lista[i][lateral_direita] = valor
            i = i + 1

        valor = valor + 1
        superior = superior + 1
        inferior = inferior - 1
        lateral_esquerda = lateral_esquerda + 1
        lateral_direita = lateral_direita - 1
    
    for i in range(n):
        lista3 = ''
        for j in range(n):
            lista3 = lista3 + ' %3d' % lista[i][j]
        print(lista3[1:])
    print('')

