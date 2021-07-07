vel = float(input('Digite a velocidade do carro em KM/H: '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Você passou acima dos limites e está sendo multado no valor de R${:.2f}'.format(multa))
else:
    print('Tudo certo, pode prosseguir!')