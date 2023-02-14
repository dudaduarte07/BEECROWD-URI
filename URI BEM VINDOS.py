#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def cara(num1, num2, num3):
    if num1 == num2 and num2 == num3:
        print(':(')
    elif num1 == num2 and num2 > num3:
        print(':(')
    elif num1 == num2 and num2 < num3:
        print(':)')
    elif num1 > num2 and num2 > num3 and (num1 - num2) <= (num2 - num3):
        print(':(')
    elif num1 > num2 and num2 > num3 and (num1 - num2) > (num2 - num3):
        print(':)')
    elif num1 < num2 and num2 < num3 and (num2 - num1) <= (num3 - num2):
        print(':)')
    elif num1 < num2 and num2 < num3 and (num2 - num1) > (num3 - num2):
        print(':(')
    elif num1 < num2 and num2 >= num3:
        print(':(')
    elif num1 > num2 and num2 <= num3:
        print(':)')

    
x = input().split()
num1, num2, num3 = x
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
res = cara(num1, num2, num3)




# 4 16 20