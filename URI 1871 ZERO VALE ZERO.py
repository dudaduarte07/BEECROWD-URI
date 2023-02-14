#!/usr/bin/env python3
# -*- coding: utf-8 -*-

while True:
    x = input().split()
    n, m = x
    n = int(n)
    m = int(m)
    if n and m != 0:
        soma = n + m
        num = str(soma)
        num = num.replace('0', '')
        print(num)
    else:
        False
        exit(0)