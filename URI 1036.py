# -*- coding: utf-8 -*-

x = input().split()
a = float(x[0])
b = float(x[1])
c = float(x[2])

delta = (b * b) - 4 * (a * c)

if delta < 0 or a == 0.0:
    print('Impossivel calcular')
else:
    raiz10 = -b + (delta ** 0.5)
    raiz20 = -b - (delta ** 0.5)
    raiz1 = raiz10 / (2 * a)
    raiz2 = raiz20 / (2 * a)
    print('R1 = %.5f' % raiz1)
    print('R2 = %.5f' % raiz2)