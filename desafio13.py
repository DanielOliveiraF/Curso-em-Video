salario = float(input('Qual o salário do Funcionário? R$ '))
reajuste = (salario * 0.15)
aumento = salario + reajuste
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, aumento))