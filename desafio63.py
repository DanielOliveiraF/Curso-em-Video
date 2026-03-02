# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os
# N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
termo = int(input('Digite quantos termos você quer apresetar da sequência de Fiboncci: '))
a1 = 0
a2 = 1
print('{} -> {}'.format(a1, a2), end='')
elementos = 3
while elementos <= termo:
    a3 = a1 + a2
    print(' -> {}'.format(a3), end='')
    a1 = a2
    a2 = a3
    elementos += 1
print(' -> FIM')
