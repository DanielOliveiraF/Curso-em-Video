# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Teceiro aluno: '))
n4 = str(input('Quarto aluno: '))
alunos = [n1, n2, n3, n4]
shuffle(alunos)
print('A ordem de apresentação será: {}'.format(alunos))