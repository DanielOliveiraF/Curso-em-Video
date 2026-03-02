# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('='*20,'Simulador de CAIXA ELETRÔNICO','='*20 )
saque = int(input('Qual valor você deseja sacar? R$ '))
total = saque
cedula = 50
totalced = 0
while True:
    if total >= cedula:
        total -= cedula
        totalced += 1
    else:
        if totalced > 0:
            print(f'Foram {totalced} de R${cedula:.2f}')
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalced = 0
        if total == 0:
            break
print('-'*20,'Saque realizado com sucesso. Tenha um bom dia!', '-'*20)