#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin


entrada = "".join(stdin.readlines())


tabela = 'sjbzpvxSJBZPVX'
out = 'fffffffFFFFFFF'
troca = str.maketrans(tabela, out)
entrada = entrada.translate(troca)

saida = ''

anterior = ''

for i in entrada:

    if i == anterior and anterior == 'f':
        saida = saida

    elif i == anterior and anterior == 'F':
        saida = saida
        
    elif i == anterior and anterior != 'F':
        saida = saida + i

    elif i == anterior and anterior != 'f':
        saida = saida + i
        
    elif i == 'f' and anterior == 'F':
        saida = saida

    elif i == 'F' and anterior == 'f':
        saida = saida
        
    else:
        saida = saida + i
        
    anterior = i
 

print(saida, end='')

exit(0)

#Letras - S, J, B, Z, P, V, X, 
