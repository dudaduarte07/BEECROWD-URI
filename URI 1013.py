# -*- coding: utf-8 -*-

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

num = (a + b + abs(a - b)) / 2
if c > num:
    maior =  c
else:
    maior = num

print("%i eh o maior" %maior)