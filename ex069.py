# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
print('-='*15,'Programa de cadastro de pessoas','-='*15)
homens = 0
mulheres_menos_de_20 = 0
pessoas_com_mais_de_18 = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa [M] para masculino e [F] para feminino: ')).strip().upper()
    while not sexo in 'MmFf':
        sexo = str(input('Sexo inválido. Digite [M] para masculino e [F] para feminino: ')).strip().upper()
    print('-'*15,'Cadastro realizado com sucesso!','-'*15)
    if sexo in 'Mm':
        homens += 1
    if idade > 18:
        pessoas_com_mais_de_18 += 1
    if sexo in 'Ff' and idade < 20:
        mulheres_menos_de_20 += 1
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while not continuar in 'SsNn':
        continuar = str(input('Opção inválida. Deseja continuar? [S/N] ')).strip().upper()
    if continuar in 'Nn':
        break
print('-'*15,'Programa de cadastro finalizado!','-'*15)
print('De acordo com os dados...')
print(f'Foram {homens} homen(s) cadastrado(s).')
print(f'Foram {pessoas_com_mais_de_18} pessoa(s) com mais de 18 anos cadastrado(s).')
print(f'Foram {mulheres_menos_de_20} mulhere(s) com menos de 20 anos cadastrada(s).')
