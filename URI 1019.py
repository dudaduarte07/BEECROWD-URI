# -*- coding: utf-8 -*-

n = int(input())
hora = n // 3600
minuto = (n - hora * 3600) // 60
segundos = n - (hora * 3600) - minuto * 60

print(hora, minuto, segundos, sep =':')