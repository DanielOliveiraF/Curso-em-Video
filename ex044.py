# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format(' LOJAS OLIVEIRA '))
preco = float(input('Preço do produto: R$ '))
pagamento = int(input('''Digite a forma de pagamento: 
[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão 
Qual das opções?'''))
print('O preço do produto é R${:.2f} e a opção de pagamento escolhida foi a {}.'.format(preco, pagamento))
if pagamento == 1:
    total = preco + (preco * 0.10)
    print('De acordo com a opção selecionada, o valor final a ser pago pelo produto será de R${:.2f}'.format(total))
elif pagamento == 2:
    total = preco - (preco * 0.05)
    print('De acordo com a opção selecionada, o valor final a ser pago pelo produto será de {:.2f} '.format(total))
elif pagamento == 3:
    parcela = preco / 2
    total = preco
    print('Sua compra parcelada em 2X, sairá no valor de R${:.2f} SEM JUROS.'.format(parcela))
    print('De acordo com a opção selecionada, o valor final a ser pago pelo produto é de R${:.2f}'.format(total))
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    parcelado = preco / parcelas + (preco / parcelas * 0.20)
    total = preco + (preco * 0.20)
    print('Sua compra parcelada em {}X, sairá no valor de R${:.2f} COM JUROS.'.format(parcelas, parcelado))
    print('De acordo com a opção, o valor final a ser pago pelo produto é de R${:.2f}'.format(total))
else:
    print('Opção inválida, tente novamente!')
