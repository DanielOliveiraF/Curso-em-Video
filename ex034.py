#  Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#  Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite o valor do salário do funcionário: R$'))
ss = salario + (salario * 0.10)
si = salario + (salario * 0.15)
if salario >= 1250:
    print('De acordo com seu salário de R${:.2f}, seu aumento será de R${:.2f}.'.format(salario, ss))
else:
    print('De acordo com seu salário de R$ {:.2f}, seu aumento será de R${:.2f}.'.format(salario, si))