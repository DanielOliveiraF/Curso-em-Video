# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Qual foi a velocidade? Km/h: '))
lu = velocidade - 80
multa = float(lu * 7)
if velocidade > 80:
    print('Ultrapassou o limite permitido!')
    print('O limite ultrapassado foi de {:.2f} Km/h a mais, e a multa será de R${:.2f}.'.format(lu, multa))
else:
    print('Não ultrapassou o limite permitido. Dirija com cuidado!')
