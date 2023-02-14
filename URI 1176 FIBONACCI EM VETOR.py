#!/usr/bin/env python3
# -*- coding: utf-8 -*-

fibonacci = [0, 1]
x = 0
y = 1
for i in range(60):
    t = x + y
    fibonacci.append(t)
    x = y
    y = t
T = int(input())
for i in range (T):
    X = int(input())
    print('Fib(%d) = %d' % (X, fibonacci[X]))