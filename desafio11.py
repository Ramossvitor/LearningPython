lar = int(input('Digite a largura da parede em metros: '))
alt = int(input('Digite a altura da parede em metros: '))
m2 = lar * alt
tinta = m2 / 2
print('Com uma parede de {} metros de largura e {} metros de altura, somando, {} metros quadrados, seriam necessarios {} litros de tinta'.format(lar, alt, m2, tinta))