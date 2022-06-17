# -*- coding utf-8 -*-

cod1, qtde1, valor1 = input().split()
cod2, qtde2, valor2 = input().split()

cod1 = int(cod1)
qtde1 = int(qtde1)
valor1 = float(valor1)

cod2 = int(cod2)
qtde2 = int(qtde2)
valor2 = float(valor2)

total1 = qtde1 * valor1
total2 = qtde2 * valor2
total = total1 + total2

print("VALOR A PAGAR: R$ %.2f" %total)
