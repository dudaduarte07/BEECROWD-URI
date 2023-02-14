# -*- coding: utf-8 -*-

valor = int(input())

nota100 = valor / 100
resto100 = valor % 100

nota50 = resto100 / 50
resto50 = resto100 % 50

nota20 = resto50 / 20
resto20 = resto50 % 20

nota10 = resto20 / 10
resto10 = resto20 % 10

nota5 = resto10 / 5
resto5 = resto10 % 5

nota2 = resto5 / 2
resto2 = resto5 % 2

nota1 = resto2 / 1

print (valor)
print ('%d nota(s) de R$ 100,00' % nota100)
print ('%d nota(s) de R$ 50,00' % nota50)
print ('%d nota(s) de R$ 20,00' % nota20)
print ('%d nota(s) de R$ 10,00' % nota10)
print ('%d nota(s) de R$ 5,00' % nota5)
print ('%d nota(s) de R$ 2,00' % nota2)
print ('%d nota(s) de R$ 1,00' % nota1)