# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
ganhou = 0
soma = 0
print('-='*15, 'PAR OU ÍMPAR', '-='*15)
while True:
    print('-'*30)
    jogador = int(input('Diga um valor: '))
    cpu = randint(0, 10)
    soma = jogador + cpu
    escolha = ' '
    while escolha not in 'PpIi':
        escolha = str(input('Digite [P] para par e [I] para ímpar: ').strip().upper())
    print('-'*30)
    if escolha == 'P' and soma % 2 == 0:
        print(f'Você jogou {jogador} e o computador jogou {cpu}. O total foi {soma} e deu PAR. ')
        print('Você venceu!')
        print('Vamos jogar novamente...')
        ganhou += 1
    elif escolha == 'I' and soma % 2 == 1:
        print(f'Você jogou {jogador} e o computador jogou {cpu}. O total foi {soma} e deu ÍMPAR. ')
        print('Você venceu!')
        print('Vamos jogar novamente...')
        ganhou += 1
    else:
        break
print('VOCÊ PERDEU!')
print('-='*30)
if soma % 2 == 0:
    print(f'Você jogou {jogador} e o computador jogou {cpu}. O total foi {soma} e deu PAR. ')
elif soma % 2 == 1:
    print(f'Você jogou {jogador} e o computador jogou {cpu}. O total foi {soma} e deu ÍMPAR. ')
print(f'GAME OVER! Você venceu {ganhou} vez(es)!')
print('-='*30)
