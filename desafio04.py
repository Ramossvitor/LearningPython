write = input('Digite Algo: ')
print('Você digitou {}, vamos te dar algumas informações sobre ele'.format(write))
print('Tipo primitivo do que você digitou', type(write))
print('Tem Só numeros? ', write.isnumeric())
print('Tem Numero ou Letra? ', write.isalnum())
print('Tem só espaços? ', write.isspace())
print('Tem só letras?', write.isalpha())
print('Está só em maiusculas? ', write.isupper())
print('Está só em minusculas? ', write.islower())
