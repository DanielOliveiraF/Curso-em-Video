# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
lista = ('Lápis', 2.20,
         'Caneta', 3.50,
         'Caderno', 10.00,
         'Mouse', 33.20,
         'Notebook', 2499.90,
         'Livro', 349.99)
print('-'*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end = '')
    else:
        print(f'R$ {lista[pos]:7.2f}')
print('-'*40)
