# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
cont = 0
numero = int(input('Digite um número: '))
for c in range(1, numero + 1):
  if numero % c == 0:
    print('\033[33m{}\033[m'.format(c), end=' ')
    cont += 1
  else:
    print('\033[31m{}\033[m'.format(c), end=' ')
if cont == 2:
  print('\nO número {} possui {} divisores, então ele é PRIMO!'.format(numero, cont))
elif cont == 1:
  print('\nO número {} possui {} divisor, então ele NÃO É PRIMO!'.format(numero, cont))
else:
  print('\nO número {} possui {} divisores, então ele NÃO É PRIMO!'.format(numero, cont))
