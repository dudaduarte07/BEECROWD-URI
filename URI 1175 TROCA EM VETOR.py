#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N = []
for i in range (20):
    x = int(input())
    N.append(x)
n = N[::-1]
for j in range (20):
    print('N[%d] = %d' % (j, n[j]))

    