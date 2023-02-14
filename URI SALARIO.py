salario = float(input())

if salario <= 2000.00:
    imp = 0
    print('Isento')
else:
    if 2000.00 < salario <= 3000.00:
        salario1 = salario - 2000.00
        imp = salario * 0.08
        
    if 3000.00 < salario <= 4500.00:
        imp1 = 0.08 * 1000.00
        salario2 = salario - 3000.00
        imp = salario2 * 0.18 + imp1
        
    if salario > 4500.00:
        imp1 = 0.08 * 1000.00
        imp2 = 0.018 * 1500.00
        salario3 = salario - 4500
        imp = imp2 + imp1 + salario3 * 0.28
        print('R$ %.2f' % imp)
