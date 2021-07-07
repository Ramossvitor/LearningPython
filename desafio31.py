dis = float(input('Digite a distancia da viagem em KMS: '))
if dis <= 200:
    valorduzen = dis * 0.5
    print('A passagem de {}KMS irá custar R${:.2f}'.format(dis, valorduzen))
else:
    valormais = dis * 0.45
    print('Pela maior distancia, o senhor está ganhando um desconto que irá fazer sua passagem custar R${}'.format(valormais))