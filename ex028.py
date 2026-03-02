# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
usuario = int(input('Digite um número entre 0 e 5: '))
computador = random.randint(0, 5) # Faz o computador sortear um número.
print('O computador escolheu {}'.format(computador))
if usuario == computador:
    print('Acertou, miserável!')
else:
    print('Errou, tente novamente!')
