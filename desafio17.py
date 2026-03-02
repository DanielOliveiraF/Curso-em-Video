# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Digite o valor do cateto oposto em cm:'))
ca = float(input('Digite o valor do cateto adjacente em cm:'))
hipotenusa = hypot(co, ca)
print('De acordo com o valor do cateto oposto {:.2f}cm e cateto adjacente {:.2f}cm, a hipotenusa será: {:.2f}cm'.format(co, ca, hipotenusa))