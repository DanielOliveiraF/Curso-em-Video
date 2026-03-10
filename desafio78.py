# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
listanum= list()
for cont in range(0, 5):
    listanum.append(int(input(f'Digite o valor da posição {cont}: ')))
print(f'Os valores digitados na lista foram: {listanum}')
print(f'O maior valor digitado na lista foi {max(listanum)} nas posições ', end = ' ')
for i, v in enumerate(listanum):
    if v == max(listanum):
        print(f'{i}...', end=' ')
print(f'\nO menor valor digitado foi {min(listanum)} nas posições', end=' ')
for i, v in enumerate(listanum):
    if v == min(listanum):
        print(f'{i}...', end=' ')