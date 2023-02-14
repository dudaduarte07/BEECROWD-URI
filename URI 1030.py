# -*- coding: utf-8 -*-

n = int(input())
cont = 0
numeros = []

for i in range (n):
    pessoas, pulos = list(map(int, input().split()))
    pulos = pulos - 1
    cont = pulos

    for j in range (pessoas):
        numeros.append(j)

    while len(numeros) > 1:
        numeros.pop(cont)
        cont = (cont + pulos) % len(numeros)

        if (cont > len(numeros)):
            cont = cont - 1

    print("Case %i: %d" %(i + 1, (numeros[0] + 1)))
    numeros.clear()