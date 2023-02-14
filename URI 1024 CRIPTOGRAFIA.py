#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import re

#n = int(input())

#for i in range(n):
#    texto = input()
#    criptografia = ''

#    for j in texto:
#        if re.match("[a-zA-Z]", j):
#            criptografia = criptografia + chr(ord(j) + 3)
#        else:
#            criptografia = criptografia + j

#    criptografia = criptografia[::-1]
#    x = len(criptografia) / 2
#    metade = int(x)
#    primeira_metade = criptografia[0:metade]
#    segunda_metade = criptografia[metade:]
#    texto_novo = ''
    
#    for j in segunda_metade:
#        texto_novo = texto_novo + chr(ord(j) - 1)

#    mensagem = primeira_metade + texto_novo

#    print(mensagem)


from math import ceil

n = int(input())

for i in range(n):
    texto_inicial = str(input())
    texto_final = ''

    for j in texto_inicial:

        if (j.isalpha() == True):
            texto_final = texto_final + chr(ord(j) + 3)
        else:
            texto_final = texto_final + j

    criptografia1 = texto_final[::-1]

    x = ceil(len(criptografia1) / 2)

    criptografia2 = criptografia1[-x:]
    criptografia3 = ''

    for k in criptografia2:
        criptografia3 = criptografia3 + chr(ord(k) - 1)
        
    result = criptografia1.replace(criptografia2, criptografia3)

    print(result)


