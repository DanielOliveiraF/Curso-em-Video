# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
distancia = float(input('Digite a distância da viagem? '))
distancia_c = distancia * 0.50
distancia_l = distancia * 0.45
print('A distância da viagem foi de {:.2f}Km'.format(distancia))
if distancia <= 200:
    print('O preço da passagem será de R${:.2f}.'.format(distancia_c))
else:
    print('O preço da passagem será de R${:.2f}.'.format(distancia_l))
