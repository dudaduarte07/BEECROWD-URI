# -*- coding utf-8 -*-

nome = str(input())
valor = float(input())
montante = float(input())

comissao = 0.15 * montante
salario = valor + comissao

print("TOTAL = R$ %.2f" %salario)