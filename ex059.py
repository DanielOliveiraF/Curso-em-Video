# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
menu = 0
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
while not menu == 5:
    print(5*'=-=', 'MENU', 5*'=-=')
    menu = int(input('''Escolha as opções: 
    [1] Somar 
    [2] Multipliciar 
    [3] Maior 
    [4] Novos números 
    [5] Sair do Programa
    Qual opção você deseja escolher? '''))
    print(15*'=-=')
    if menu == 1:
        soma = a + b
        print('A soma entre {} + {} vale {}'.format(a, b, soma))
    elif menu == 2:
        mult = a * b
        print('A multiplicação entre {} x {} vale {}'.format(a, b, mult))
    elif menu == 3:
        if a > b:
            maior = a
        elif a < b:
            maior = b
            print('Entre {} e {} o maior vale {}'.format(a, b, maior))
        else:
            print('Os valores digitados são iguais!')
    elif menu == 4:
        print('Digite novamente os valores! ')
        a = int(input('Digite novamente o primeiro valor: '))
        b = int(input('Digite novamente o segundo valor: '))
    elif menu == 5:
        print('FINALIZANDO...')
        sleep(1)
        print('Programa finalizado com sucesso!')
    else:
        print('Opção inválida, tente novamente!')
