# Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
valores = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        valores[0].append(n)
    if n % 2 == 1:
        valores[1].append(n)
print(f'Os valores pares digitados foram: {sorted(valores[0])}')
print(f'Os valores impares digitados foram: {sorted(valores[1])}')