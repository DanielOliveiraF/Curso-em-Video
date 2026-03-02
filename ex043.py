# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida
peso = float(input('Digite seu peso? (Kg)'))
altura = float(input('Digite sua altura? (m)'))
imc = peso / (altura ** 2)
print('De acordo com seu peso {:.2f}Kg, e sua altura {:.2f}m, seu IMC é: {:.2f}'.format(peso, altura, imc))
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc <= 25:
    print('Você está no peso IDEAL!')
elif imc >= 25 and imc <= 30:
    print('Você está em SOBREPESO!')
elif imc >= 30 and imc <= 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MORBIDA!')
    