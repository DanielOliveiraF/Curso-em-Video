# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = list()
cont = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    lista.sort(reverse=True)
    cont += 1
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
    while continuar not in 'SN':
        continuar = str(input('Digitação inválida. Quer continuar? [S/N] ')).strip().upper()
print('-='*30)
print(f'Você digitou {cont} elementos!')
print(f'Os valores digitados em ordem decrescente foram {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não está prisente na lista!')
