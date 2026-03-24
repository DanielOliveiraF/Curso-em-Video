# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
temp = list()
principal = list()
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(principal) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    principal.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Digitação inválida. Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('-='*30)
print(f'Lista das pessoas: {principal}')
print(f'Foram cadastradas {len(principal)} pessoas.')
print(f'O maior peso cadastrado foi {mai:.2f} Kg. As pessoas com esse peso foram: ', end='')
for p in principal:
    if p[1] == mai:
        print(f'[{p[0]}]', end = ' ')
print(f'\nO menor peso cadastrado foi {men:.2f} Kg. As pessoas com esse peso foram: ', end='')
for p in principal:
    if p[1] == men:
        print(f'[{p[0]}]', end = ' ')