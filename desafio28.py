import random
aleatorio = int(random.choice(range(1, 6)))
tentativa = int(input('Digite um numero: '))
if tentativa == aleatorio:
    print('Parabéns, você acertou! Eu pensei no {} e você também!'.format(aleatorio))
else:
    print('Não foi dessa vez! Eu pensei no {} e você no {}'.format(aleatorio, tentativa))