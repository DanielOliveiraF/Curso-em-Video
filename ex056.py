# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somaidade = 0
mediaidade = 0
homemmaisvelho = ''
idadehomemmaisvelho = 0
mulhermenor = 0
for c in range(1, 5):
    nome = str(input('Digite o nome da pessoa: ')).strip().title()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite o sexo da pessoa [M] ou [F]: ')).strip().upper()
    somaidade += idade
    if c == 1 and sexo in 'M':
        homemmaisvelho = nome
        idadehomemmaisvelho = idade
    if idadehomemmaisvelho < idade and sexo in 'M':
        homemmaisvelho = nome
        idadehomemmaisvelho = idade
    if sexo in 'F' and idade < 20:
        mulhermenor += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho da lista se chama {} e tem {} anos de idade.'.format(homemmaisvelho, idadehomemmaisvelho))
print('Nessa lista, temos {} mulher(es) menor de 20 anos. '.format(mulhermenor))




