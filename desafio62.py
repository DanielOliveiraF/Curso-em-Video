# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
c = 0
valortotal = 0
mais = 10
while mais != 0:
    valortotal += mais
    while c < valortotal:
        print('{} ->'.format(termo), end=' ')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos deseja mais? '))
print('Foram {} termos a mais adicionados.'.format(valortotal))