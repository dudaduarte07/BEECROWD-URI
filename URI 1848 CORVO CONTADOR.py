#!/usr/bin/env pyhton3
# -*- coding: utf-8 -*-

# piscada é um numero binario
# 1 olho aberto significa 1
# 1 olho fechado significa 0
# olho da esquerda +++
# olho da direita +
# a cada piscada esse numero deve ser somado
# a cada grito essa soma é um resultdao
# grito == caw caw
# 1 piscada == 3 caract *(olho aberto) ou - (olho fechado) da esquerda p dir
# o corvo tem 3 olhos

def transformar (piscada):
    piscada = piscada.replace('-', '0')
    piscada = piscada.replace('*', '1')
    return piscada

def decimal(piscada):
    decimal = 0
    potencia = 0
    while piscada > 0:
       digito = piscada % 10
       num = digito * (2 ** potencia)
       decimal = decimal + num
       potencia = potencia + 1
       piscada = piscada // 10
    return decimal

contador = 0
soma = 0
while contador < 3:
    piscada = input()
    if piscada != 'caw caw':
        piscada = transformar(piscada)
        piscada = int(piscada)
        piscada = decimal(piscada)
        soma = soma + piscada
    else:
        print(soma)
        contador = contador + 1
        soma =  0