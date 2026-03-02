# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome completo: ')).strip().title()
print('É um prazer te conhecer!')
print('Primeiro nome: {}'.format(nome.split()[0]))
print('Último nome: {}'.format(nome.split()[-1]))