import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digte o comprimento do cateto adjacente: '))
co2 = co * co
ca2 = ca * ca
juncoca2 = co2 + ca2
hipotenusa = math.pow(juncoca2, 1/2)
print('O resultado da hipotenusa com o cateto oposto sendo {} e o cateto adjacente sendo {} é {:.2f}'.format(co, ca, hipotenusa))

#Ou também pode ser feito importando o seguinte 'from math import hypot e o codigo ficaria
#co = float ...
#ca = float ...
#hi = hypot(co, ca)
#
