# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes
print('-='*30)
print(' '*15,'Analisador de Triângulos!')
print('-='*30)
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('De acordo com os segmentos a: {:.2f}, b: {:.2f} e c: {:.2f} da para formar um triângulo.'.format(a, b, c))
else:
    print('De acordo com os segmentos a: {:.2f}, b: {:.2f} e c: {:.2f} NÃO da para formar um triângulo.'.format(a, b, c))
    exit()
if a == b == c:
    print('O triângulo é EQUILÁTERO. ')
elif a == b !=c or a == c !=b or b == c !=a:
    print('O triângulo é ISÓSCELES.')
elif a !=b !=c or b !=c !=a or c !=a !=b:
    print('O triângulo é ESCALENO.')
