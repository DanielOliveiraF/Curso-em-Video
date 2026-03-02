# A Confederação Nacional de Natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
from datetime import date
atleta = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - atleta
print('O ano em que o atleta nasceu foi em {} e ele possui {} anos.'.format(atleta, idade))
if idade <= 9:
    print('O atleta irá disputar na categoria MIRIM.')
elif idade <= 14:
    print('O atleta irá disputar na categoria INFANTIL.')
elif idade <= 19:
    print('O atleta irá disputar na categoria JÚNIOR.')
elif idade <= 25:
    print('O atleta irá disputar na categoria SÊNIOR.')
else:
    print('O atleta irá disputar na categoria MASTER.')
