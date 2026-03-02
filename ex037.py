# Escreva um programa em Python que leia um número inteiro qualquer e peça para o
# usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um numero inteiro: '))
base = str(input('Digite em qual base você quer converter (binário, octal ou hexadecimal):')).strip().lower()
opcoes = ['binario' , 'binário', 'octal', 'hexadecimal']
binário = bin(numero)
binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)

if base not in opcoes:
    print('A conversão que você escolheu não é válida, talvez tenha sido erro de digitação. Tente novamente!')
elif base == 'binario' or base == 'binário':
    print('A conversão do número {} para binário é: {}'.format(numero, binario[2:] or binário[2:]))
elif base == 'octal':
    print('A conversão do número {} para octal é: {}'.format(numero, octal[2:]))
else:
    print('A conversão do número {} para hexadecimal é: {}'.format(numero, hexadecimal[2:]))