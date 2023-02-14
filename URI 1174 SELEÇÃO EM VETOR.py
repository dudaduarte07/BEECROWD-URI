#!/usr/bin/env python3
# -*- coding: utf-8 -*-


x = 0
while x < 100:
    n = input()
    n = float(n)
    if n <= 10.0:
        print('A[%d] = %.1f' % (x, n))
    x = x + 1

#A = []
#for _ in range (100):
#    x = float(input())
#    A.append(x)
#    if x <= 10.0:
#        print('A[%d] = %.1f' % (i, x))