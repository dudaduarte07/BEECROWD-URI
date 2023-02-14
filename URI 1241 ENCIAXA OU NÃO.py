#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#def conta_digito(n):
#    n = int(n)
#    contador = 0
#    while n > 0:
#        n = n // 10
#        contador = contador + 1
#    return contador


#n = int(input())
#x = input().split()
#a, b = x
#a = int(a)
#b = int(b)
#qtde = 0

#while qtde < n:
#    compb = conta_digito(b)
#    contador = 0
#    while contador < compb:
#        aa = a % 10
#        bb = b % 10
#        if aa == bb:
#            contador = contador + 1
#        else:
#            contador == compb
#            print('nao encaixa')
#        qtde = qtde + 1
#        a = a // 10
#        b = b // 10
#    print('encaixa')

n = int(input())

while n > 0:
    n = n - 1
    x = input().split()
    a, b = x
    comp_a = len(a)
    comp_b = len(b)
    if comp_a < comp_b:
        resposta = 'nao encaixa'
    else:
        if (a[comp_a - comp_b::] == b):
            resposta = 'encaixa'
        else:
            resposta = 'nao encaixa'
    print(resposta)
