# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
lista = []
par = []
impar = []
while True:
    valor = (int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    lista.append(valor)

    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

    while continuar not in 'SN':
        continuar = str(input('Digitação inválida. Quer continuar? [S/N] ')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'A lista completa: {lista}')
print(f'A lista de números pares: {par}')
print(f'A lista de números impares: {impar}')