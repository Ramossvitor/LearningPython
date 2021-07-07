a = float(input('Digite um numero: '))
b = float(input('Digite outro numero: '))
c = float(input('Digite o terceiro numero: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#Verificando maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor inserido foi o {} e o maior valor inserido foi o {}'.format(menor, maior))