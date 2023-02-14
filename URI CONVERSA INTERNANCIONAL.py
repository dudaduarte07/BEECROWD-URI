#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
contador1 = 0
while contador1 < n:
  pessoas = int(input())
  contador1 = contador1 + 1
  contador2 = 0
  while contador2 < pessoas:
    lingua1 = input()
    contador2 = contador2 + 1
    while contador2 < pessoas:
      lingua = input()
      contador2 = contador2 + 1
      if lingua1 != lingua:
        fala = 'ingles'
      if lingua1 == lingua and lingua1 == lingua1:
        fala = lingua1
      else:
        fala = 'ingles'
    print(fala)
