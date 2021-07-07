tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--Fim--')

##Ou fazer o seguinte, para simplificar

gain = int(input('Quantos anos tem seu carro? '))
print('Carro novo'if gain <=3 else'Carro Velho')