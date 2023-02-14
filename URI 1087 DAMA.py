#!/usr/bin/env python3
# -*- coding: utf-8 -*-

while True:
    valores = input().split(' ')
    x1, y1, x2, y2 = valores

    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    x = abs(x1 - x2)
    y = abs(y1 - y2)

    if x1 + y1 + x2 + y2 == 0:
        False
        exit(0)
    if x1 == x2 and y1 == y2:
        d = 0
        print(d)
    elif x1 == x2 or y1 == y2:
        d = 1
        print(d)
    elif x == y:
        d = 1
        print(d)
    else:
        d = 2
        print(d)