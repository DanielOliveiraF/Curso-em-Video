# Crie um programa que faça o computador jogar Jokenpô com você.
# Nome do game - "Jo" - "Ken" - "Po"!

from random import choice
from time import sleep

print('\n')
print('\33[;32m-=-\33[m'*12)
print(' '*9,'\33[;33m"Jo - Ken - Pô!"\33[m')
print('\33[;32m-=-\33[m'*12,'\n')

print('-*-'*5, 'REGRAS!', '-*-'*5)
print('''\33[;35m\nAs regras do Jo-Ken-Pô (ou Pedra, Papel e Tesoura) são as seguintes:
Pedra ganha da Tesoura, Tesoura ganha do Papel e Papel ganha da Pedra.
O usuário digita uma das três opções citadas, enquanto a máquina decide qual das três opções jogar. 
Após a contagem, quem escolher a opção que vence a do outro ganha a rodada. 
Caso ambos selecionem a mesma opção, ocorre um empate. \33[m''')

# Início do jogo

jogador = str(input('\33[4m\nDigite entre as opções "Pedra", "Papel", "Tesoura" para iniciar o jogo\33[m: ')).strip().lower()
opcoes = ('pedra','papel', 'tesoura')
cpu = choice(opcoes)

# Verificando se o usuário digitou as opções

# Caso ele digite algo errado

if jogador not in opcoes:
    print('\33[;31m\nVOCÊ NÃO ESCOLHEU A OPÇÃO CORRETA, TENTE NOVAMENTE!\33[m')
    exit()

# Caso ele digite certo
else:
    print('\33[;33m\nJO\33[m')
    sleep(1)
    print('\33[;33m\nKEN\33[m')
    sleep(1)
    print('\33[;33m\nPÔ!\33[m')
    sleep(1)

# Imprimindo resultados

print('\33[;35m\nCPU escolheu "{}"!\33[m'.format(cpu.upper()))

# Caso ele digite corretamente

if jogador == cpu:
    print('\33[;36m\nEMPATE!\33[m')

elif jogador == 'pedra' and cpu == 'tesoura' or jogador == 'papel' and cpu == 'pedra' or jogador == 'tesoura' and cpu == 'papel':
    print('\33[;32m\nJOGADOR venceu, Parabéns!\33[m')

else:
    print('\33[;33m\nA CPU venceu, tente novamente!\33[m')

print('\n')
print('\33[;32m-=-\33[m'*12)
print(' '*13,'\33[;33m"FIM!"\33[m')
print('\33[;32m-=-\33[m'*12,'\n')
