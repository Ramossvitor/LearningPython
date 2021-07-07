from random import choice
nome1 = str(input('Digite o nome do primeiro aluno: '))
nome2 = str(input('Digite o nome do segundo aluno: '))
nome3 = str(input('Digite o nome do terceiro aluno: '))
lista = [nome1, nome2, nome3]
escolhido = choice(lista)
print('O aluno escolhido foi o {}, ele(a) foi escolhido pela nossa inteligencia artificial randomica'.format(escolhido))


