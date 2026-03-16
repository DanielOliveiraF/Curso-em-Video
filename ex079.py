# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        lista.sort()
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado. Por favor, digite um valor válido.')
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('-='*30)
print(f'Sua lista digitada em ordem crescente: {lista}')
