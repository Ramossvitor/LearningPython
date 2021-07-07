n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
nota = (n1 + n2)/2
print('Sua média é de {:.2f}'.format(nota))
if nota >= 8.3:
    print('Boa média garoto! continue assim!')
if ((nota >=7.0) and (nota < 8.3)):
    print('Está na média! Pode estudar mais!')
if nota <= 6.9:
    print('Abaixo da média, estuda mais porra!')