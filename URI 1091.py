# -*- coding: utf-8 -*-

while True:
    k = int(input())

    n, m = input().split()
    n = int(n)
    m = int(m)
    cont = 0

    if k == 0:
        break

    while cont < k:
        x, y = input().split()
        x = int(x)
        y = int(y)

        if x > n and y > m:
            print('NE')

        elif x > n and y < m:
            print('SE')

        elif x < n and y > m:
            print('NO')

        elif x < n and y < m:
            print('SO')

        elif x == n or y == m:
            print('divisa')

        cont = cont + 1


arruamr