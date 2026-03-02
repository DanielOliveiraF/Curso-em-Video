# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
p = str(input('Primeiro aluno: '))
s = str(input('Segundo aluno: '))
t = str(input('Terceiro aluno: '))
q = str(input('Quarto aluno: '))
aluno = choice([p, q, s, t])
print('O aluno escolhido foi {}'.format(aluno))