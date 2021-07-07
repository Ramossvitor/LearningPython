nome = str(input('Digite seu nome: ')).strip().upper()
separar = nome.split()
if separar[0] == 'VITOR':
    print('Que nome lindo você tem {}'.format(nome))
else:
    print('Seu nome é tão.... normal.')
    print('O nome {} é tão feio'.format(nome))