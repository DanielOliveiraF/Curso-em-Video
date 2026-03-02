# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
print('-' * 30, 'TABUADA', '-'*30)
print('-' * 30, 'Instruções:', '-'*30)
print('**','Digite qualquer valor para saber sua tabuada. Caso digite um valor negativo, o programa será encerrado.','**')
while True:
    num = int(input('Digite um valor para saber sua tabuada: '))
    print('-'*30)
    if num < 0:
        break
    for n in range(1, 11):
        print(f'{num} x {n:2} = {num * n}')
    print('-'*30)
print('Programa TABUADA finalizado com sucesso!')