# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora
# exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
ano_de_nascimento = int(input('Digite o seu ano de nascimento: '))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_de_nascimento
print('Quem nasceu em {} tem {} anos.'.format(ano_de_nascimento, idade))
if idade < 18:
    tempo = 18 - idade
    alistamento = ano_atual + tempo
    print('Você ainda não está na idade de se alistar, ainda faltam {} anos.!'.format(tempo))
    print('O ano do seu alistamento é em {}'.format(alistamento))
elif idade == 18:
    print('VOCÊ ESTÁ NA IDADE DE SE ALISTAR!')
elif idade > 18:
    tempo = 18 - idade
    alistamento = ano_atual + tempo
    print('Você já passou da idade de se alistar há {} anos.'.format(abs(tempo)))
    print('O ano do seu alistamento foi em {}'.format(alistamento))
