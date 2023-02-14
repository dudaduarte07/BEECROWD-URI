#!/usr/bin/env python3
# -*- coding: utf-8 -*-

loop = True
while loop == True:
    digito, valor = input().split()

    if valor == '0' and digito == '0':
        loop = False
    
    else:
        x = valor.count(digito)
        troca = False

        while troca == False:
            valor = valor.replace(digito, '')
            if valor == '':
                saida = 0
                print(saida)
                troca = True
            else:
                valor = int(valor)
                print(valor)
                troca = True

exit(0)

