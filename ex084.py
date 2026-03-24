# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
dados = list()
pessoas = list()
cont = 0
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    cont += 1
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    print('Cadastro realizado com sucesso!')
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Dado inválido. Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 30)
print(f'Os dados foram {pessoas}')
print(f'Foram cadastradas {cont} pessoas!')
print(f'O maior peso foi de {mai:.2f} Kg. As pessoas com esse peso foram: ', end ='|')
for p in pessoas:
    if p[1] == mai:
        print(f'{p[0]}', end='|')
print(f'\nO menor peso foi de {men:.2f} Kg. As pessoas com esse peso foram: ', end = '|')
for p in pessoas:
    if p[1] == men:
        print(f'{p[0]}', end='|')


