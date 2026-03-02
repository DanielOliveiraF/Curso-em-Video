# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
from time import sleep

casa = float(input('Qual é o valor do imóvel? R$ '))
salario = float(input('Qual é o salário do comprador? R$ '))
anos = int(input('Quantos anos de financiamento? '))

print('O valor da casa é de R${:.2f}.'.format(casa))
print('O salário da pessoa é de R${:.2f}.'.format(salario))
print('A pessoa pretende pagar a casa em {} anos.'.format(anos))

prestacao = casa / (anos*12)

print('PROCESSANDO INFORMAÇÕES...')
sleep(3)

if prestacao <= salario * 0.30:
    print('De acordo com o salário R${:.2f} e o valor das prestações R${:.2f},'.format(salario, prestacao), end='')
    print('seu emprestimo foi APROVADO!')
else:
    print('Infelizmente, de acordo com seu salário R${:.2f} e o valor das prestações R${:.2f},'.format(salario, prestacao), end='')
    print('seu empréstimo foi NEGADO!')