# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
valor = int(input('Digite um valor: '))
c = valor
f = 1
print('Calculando o fatorial de {}!'.format(valor), end = ' = ')
while c > 0:
    print('{}'. format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f = f * c
    c -= 1
print('{}'.format(f))