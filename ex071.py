# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$100, R$50, R$20, R$10, R$5, R$2 e R$1.
print('='*20,' SIMULADOR DE CAIXA ELETRÔNICO ','='*20)
saque = int(input('Qual o valor você que sacar? R$ '))
total = saque
cedula = 100
totcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        if totcedula > 0:
            print(f'Você sacou {totcedula} cédulas de R$ {cedula}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        totcedula = 0
        if total == 0:
            break
print('-'*20,'Saque realizado com sucesso! Tenha um bom dia!','-'*20)