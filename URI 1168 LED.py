#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#n = int(input())
#contador = 0
#led = 0
#while contador < n:
#    num = int(input())
#    if num == 0:
#        led = led + 6
#    while num > 0:
#        numero = num % 10
#        if numero == 1:
#            led = led + 2
#        if numero == 2:
#            led = led + 5
#        if numero == 3:
#            led = led + 5
#        if numero == 4:
#            led = led + 4
#        if numero == 5:
#            led = led + 5
#        if numero == 6:
#            led = led + 6
#        if numero == 7:
#            led = led + 3
#        if numero == 8:
#            led = led + 7
#        if numero == 9:
#            led = led + 6
#        if numero == 0:
#            led = led + 6
#        num = num // 10
#    contador = contador + 1
#    print(led, 'leds')
#    led = 0

n = int(input())

for i in range(1, n + 1):
    led = 0
    num = input()
    for j in range(0, len(num)):
        if num [j] == '1':
            led = led + 2
        if num [j] == '2':
            led = led + 5
        if num [j] == '3':
            led = led + 5
        if num [j] == '4':
            led = led + 4
        if num [j] == '5':
            led = led + 5
        if num [j] == '6':
            led = led + 6
        if num [j] == '7':
            led = led + 3
        if num [j] == '8':
            led = led + 7
        if num [j] == '9':
            led = led + 6
        if num [j] == '0':
            led = led + 6
    print(led, 'leds')