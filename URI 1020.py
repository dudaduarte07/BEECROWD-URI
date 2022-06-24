# -*- coding: utf-8 -*-

numero = int(input())
ano = numero // 365
meses = (numero - ano * 365) // 30
dias = numero - (ano * 365) - meses * 30

print ('%d ano(s)' % (ano))
print ('%d mes(es)' % (meses))
print ('%d dia(s)' % (dias))