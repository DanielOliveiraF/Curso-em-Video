# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input('Digite seu nome completo: ')).strip()
print('Tem "{}" no nome? {}'.format('Silva', 'SILVA' in nome.upper()))
