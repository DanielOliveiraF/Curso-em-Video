real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.52
euro = real / 6.47
print('Com R${:.2f} você pode comprar US${:.2f} e {:.2f}€'.format(real, dolar, euro))