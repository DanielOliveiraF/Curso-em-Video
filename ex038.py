# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais
x = int(input('Digite o primeiro valor inteiro: '))
y = int(input('Digite o segundo valor inteiro: '))

if x == y:
    print('Não existe valor MAIOR, os dois são IGUAIS.')
elif x > y:
    print('O PRIMEIRO valor é maior.')
else:
    print('O SEGUNDO valor é maior.')