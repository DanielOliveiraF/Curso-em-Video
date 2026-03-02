# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    valor = int(input('Digite um valor entre 0 e 20: '))
    while valor not in range(0, 21):
        valor = int(input('Tente novamente. Digite um valor novamente entre 0 e 20: '))
    print(f'Você digitou o valor {numeros[valor]}.')
    break
