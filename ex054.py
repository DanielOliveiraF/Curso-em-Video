# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
cont_a = 0
cont_b = 0
for c in range(1, 8):
    nasc = int(input('Ano de nascimento da pessoa {}: '.format(c)))
    atual = date.today().year
    idade = atual - nasc
    if idade >= 18:
        cont_a += 1
    else:
        cont_b += 1
print('De acordo com os anos registrados, {} pessoas atingiram a maioridade.'.format(cont_a))
print('Além disso, pelos dados registrados, {} pessoas não atingiram a maioridade.'.format(cont_b))
