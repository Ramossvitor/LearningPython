salario = float(input('Digite seu salário: '))
if salario >= 1250:
    aumaior = salario * 1.1
    print('Seu aumento irá fixar seu salário em R${:.2f}'.format(aumaior))
else:
    aumenor = salario * 1.15
    print('Seu aumento irá fixar seu salário em R${:.2f}'.format(aumenor))
