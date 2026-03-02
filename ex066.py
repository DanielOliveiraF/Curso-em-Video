# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
s = 0
c = 0
while True:
    numero = int(input('Digite um valor (999 encerra o programa): '))
    if numero == 999:
        break
    s += numero
    c += 1
print(f'A soma dos {c} valores foi de {s}.')