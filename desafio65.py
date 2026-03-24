# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
sair = ''
cont = 0
maior = 0
menor = 0
soma = 0
while not sair == 'N':
    num = int(input('Digite um número inteiro: '))
    sair = str(input('Deseja continuar [S/N]? ')).strip().upper()
    soma += num
    cont += 1
    media = soma / cont
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('Você digitou {} valores. A média dos valores é de {}.'.format(cont, media))
print('O maior valor lido foi {} e o menor valor lido foi {}.'.format(maior, menor))