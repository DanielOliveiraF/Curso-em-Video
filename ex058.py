# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
from random import randint
cpu = randint(0, 10)
print('Sou seu computador...')
print('Acabei de pensar em um numero entre 0 e 10.')
print('Será que você consegue adivinhar?')
jogador = int(input('Escolha um número de 0 a 10: '))
tentativas = 1
while jogador != cpu:
    if jogador > cpu:
        jogador = int(input('Você errou, o valor é menor. Escolha novamente de 0 a 10: '))
        tentativas += 1
    else:
        jogador = int(input('Você errou, o valor é maior. Escolha novamente de 0 a 10: '))
        tentativas += 1
if tentativas == 1:
    print('Você é parente do professor Xavier, não é possívis, de primeira. Parabéns!')
elif tentativas <= 5:
    print('Você acertou. Mas precisou de {} tentativas, tente diminuir na próxima.'.format(tentativas))
else:
    print('Meu Deus, se esforce mais! Você precisou de {} tentativas kkkkkkkk.'.format(tentativas))