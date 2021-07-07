ano = int(input('Digite o ano que você quer saber: '))
paim = ano % 4
if paim == 0:
    print('Sim, {} foi, ou será um ano bissexto'.format(ano))
else:
    print('Não, {} não foi/será, um ano bissexto'.format(ano))