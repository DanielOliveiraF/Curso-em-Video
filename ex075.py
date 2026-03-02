# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
a = b = c = d = 0
while True:
    n = int(input('Digite um valor: '))
    a += n
    n = int(input('Digite mais valor: '))
    b += n
    n = int(input('Digite outro valor: '))
    c += n
    n = int(input('Digite o último valor: '))
    d += n
    break
n = (a, b, c, d)
print(f'Os valores digitados foram: {n}')
print(f'O valor 9 apareceu {n.count(9)} veze(s)')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')
