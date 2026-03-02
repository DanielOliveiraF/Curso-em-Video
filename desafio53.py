# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:
print('O inverso de {} é {}'.format(frase, frase[::-1]))
for letra in range(len(frase)-1, -1, -1):
    if frase[letra] == frase[letra-1]:
        print('\nA frase digitada é um Palíndromo!')
if frase != frase[::-1]:
    print('\nA frase digitada não é um palíndromo!')
print('\nFim')