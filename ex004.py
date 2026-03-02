a = input('Digite algo: ')
print('Só tem espaços? {}'.format(a.isspace()))
print('É um número? {}'.format(a.isnumeric()))
print('É alfabetico? {}'.format(a.isalpha()))
print('É alfanumérico? {}'.format(a.isalnum()))
print('Está em maiúsculas? {}'.format(a.isupper()))
print('Está em minúsculas? {}'.format(a.islower()))
print('Está capitalizada? {}'.format(a.istitle())) # Não está nem maiúscula e nem minúscula.