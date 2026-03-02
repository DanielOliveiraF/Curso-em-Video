# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo sem considerar espaços.
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('Nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('Nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome é {} e tem {} letras.'.format(nome.split()[0], nome.find(' ')))