#!/usr/bi/env python3
# -*- coding: utf-8 -*-

def maior_palavra(p):
    numero_elementos = len(p)
    posicao = 0
    palavra_maior = 0
    maior_palavra = ''

    while posicao < numero_elementos:
        palavra = p[posicao]
        tamanho_palavra = len(palavra)

        if tamanho_palavra > palavra_maior:
            palavra_maior = tamanho_palavra
            maior_palavra = palavra

        posicao = posicao + 1

    return maior_palavra

x = True
y = True

while x == True:
    n = int(input())

    if n == 0:
        x = False
    else:
        lista = []
        for _ in range(n):
            lista.append(input())
        maior = maior_palavra(lista)
        qtde_palavras = len(lista)
        posicao = 0

        if not y:
            print('')
        else:
            y = False
        while posicao < qtde_palavras:
            atual = lista[posicao]
            nova = ''
            if atual == maior:
                print(atual)
            else:
                espacos = len(maior) - len(atual)
                for esp in range(espacos):
                    nova = nova + ' '
                nova = nova + atual
                print(nova)

            posicao = posicao + 1


