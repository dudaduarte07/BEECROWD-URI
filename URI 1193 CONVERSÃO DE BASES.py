#!/usr/bi/env python3
# -*- coding: utf-8 -*-

#binario - decimal *certo*
def bin_to_dec(n):
    n = int(n)
    digito = 0
    soma = 0
    while n > 0:
        numero = n % 10
        if numero == 1:
            x = 1 * (2 ** digito)
        else:
            x = 0 * (2 ** digito)
        n = n // 10
        soma = soma + x
        digito = digito + 1
    return soma

        
# decimal - hexadecimal *certo*
def dec_to_hex(n):
    n = int(n)
    hexadecimal = ''
    while n > 0:
        resto = n % 16
        if resto > 9:
            digito = chr(87 + resto)
            hexadecimal = hexadecimal + digito
        else:
            resto = str(resto)
            hexadecimal = hexadecimal + resto
        n = n // 16
    hexadecimal = hexadecimal[::-1]
    return hexadecimal

# decimal - binario *certo*
def dec_to_bin(n):
    decimal = int(n)
    soma = 0
    contador = 0
    while decimal > 0:
        binario = decimal % 2
        soma = soma + binario * (10 ** contador)
        contador = contador + 1
        decimal = decimal // 2
    return soma

        
# hexadecimal - decimal *certo*
def hex_to_dec(n):
    x = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
        'a', 'b', 'c', 'd', 'e', 'f']
    nlista = list(n) #passa para lista 
    resultado = 0
    for pos, digito in enumerate(nlista[-1::-1]): 
        posicao = x.index(digito)
        resultado = (int(posicao) * (16**pos)) + resultado
    return(resultado)


qtde = int(input())
contador = 1
while contador <= qtde:
    n, s = input().split()
    n, s = str(n), str(s)
    if s == 'bin':
        res1 = bin_to_dec(n)
        res2 = dec_to_hex(res1)
        print('Case %d:' % contador)
        print('%d dec' % res1)
        print('%s hex' % res2)
        print('')
    if s == 'dec':
        res1 = dec_to_hex(n)
        res2 = dec_to_bin(n)
        print('Case %d:' % contador)
        print('%s hex' % res1)
        print('%d bin' % res2)
        print('')
    if s == 'hex':
        res1 = hex_to_dec(n)
        res2 = dec_to_bin(res1)
        print('Case %d:' % contador)
        print('%d dec' % res1)
        print('%d bin' % res2)
        print('')
    contador = contador + 1
