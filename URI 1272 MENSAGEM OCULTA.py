#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
contador = 0

while contador < n:
    texto = input()
    lista1 = texto.split()
    saida = ''
    posicao = 0
    x = len(lista1)
    while posicao < x:
        palavra = lista1[posicao]
        letra = palavra[0]
        saida = saida + letra
        posicao = posicao + 1
    contador = contador + 1
    print(saida)
