# -*- coding: utf-8 -*-
#!/usr/bin/env python3

N = float(input())

nota100 = N // 100
resto = N % 100

nota50 = resto // 50
resto = resto % 50

nota20 = resto // 20
resto = resto % 20

nota10 = resto // 10
resto = resto % 10

nota5 = resto // 5
resto = resto % 5

nota2 = resto // 2
resto = resto % 2

moeda1 = resto // 1
resto = resto % 1

moeda50 = (resto * 100) // 50
resto = (resto * 100) % 50

moeda25 = resto // 25
resto = resto % 25

moeda10 = resto // 10
resto = resto % 10

moeda5 = resto // 5
resto = resto % 5

moeda01 = resto // 1
resto = resto % 1

print('NOTAS:')
print('%i nota(s) de R$ 100.00' % (nota100))
print('%i nota(s) de R$ 50.00' % (nota50))
print('%i nota(s) de R$ 20.00' % (nota20))
print('%i nota(s) de R$ 10.00' % (nota10))
print('%i nota(s) de R$ 5.00' % (nota5))
print('%i nota(s) de R$ 2.00' % (nota2))
print('MOEDAS:')
print('%i moeda(s) de R$ 1.00' % (moeda1))
print('%i moeda(s) de R$ 0.50' % (moeda50))
print('%i moeda(s) de R$ 0.25' % (moeda25))
print('%i moeda(s) de R$ 0.10' % (moeda10))
print('%i moeda(s) de R$ 0.05' % (moeda5))
print('%i moeda(s) de R$ 0.01' % (moeda01))