# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
print('-='*15,'MERCADINHO DO DANIEL','-='*15)
nomedoproduto = ''
produto_mais_de_1000 = 0
totalgasto = 0
produtomaisbarato = 0
cont = 0
while True:
    produto = str(input('Digite o nome do produto: ')).strip().upper()
    valor = float(input('Digite o valor do produto R$: '))
    print('-='*15,'PRODUTO ADICIONADO COM SUCESSO!','-='*15)
    totalgasto += valor
    cont += 1
    if valor > 1000:
        produto_mais_de_1000 += 1
    if cont == 1:
        produtomaisbarato = valor
        nomedoproduto = produto
    else:
        if valor < produtomaisbarato:
            produtomaisbarato = valor
            nomedoproduto = produto
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
    while not continuar in 'SsNn':
        continuar = str(input('Opção inválida! Quer continuar? [S/N] ')).strip().upper()
print('-='*15,'COMPRA FINALIZADA!','-='*15)
print(f'O total gasto em suas compras foi de R$ {totalgasto:.2f}')
print(f'Foram {produto_mais_de_1000} produto(s) comprados que custam mais de R$ 1000,00.')
print(f'O produto mais barato comprado foi "{nomedoproduto}" no valor de R$ {produtomaisbarato:.2f}.')
