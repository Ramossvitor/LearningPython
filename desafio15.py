kmrodado = float(input('Quantos Kilometros foram rodados com esse carro? '))
dialugado = float(input('A quantos dias ele está com você?'))
precodia = dialugado * 60
precokm = kmrodado * 0.15
totalpagar = precokm + precodia
print('Com {}KMs rodados e {} Dias alugados, você deve pagar R${} para a Localiza Veiculos'.format(kmrodado, dialugado, totalpagar))