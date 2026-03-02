# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-='*30)
print('Analisador de Triângulos!')
print('-='*30)
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('De acordo com os segmentos {:.2f}, {:.2f} e {:.2f}, dá para formar um triângulo.'. format(a,b,c))
else:
    print('De acordo com os segmentos {:.2f}, {:.2f} e {:.2f}, não da para formar um triângulo.'. format(a,b,c))
