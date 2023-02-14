#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
x = 0
while x < 10:
    if x == 0:
        n = n
    else:
        n = n * 2
    print('N[%d] = %d' % (x, n))
    x = x + 1