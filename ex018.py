# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
angulo = float(input('Digite o valor do ângulo: '))
seno = sin(radians(angulo))
co = cos(radians(angulo))
tan = tan(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, co))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tan))