frase = str(input('Digite algo: ')).strip()
print('A letra "A" aparece {} vezes na frase "{}"'.format(frase.upper().count('A'), frase))
print('A primeira letra "A" apareceu na posição {} e a ultima, apareceu na posição {}'.format(frase.upper().find('A')+1, frase.upper().rfind('A')+1))