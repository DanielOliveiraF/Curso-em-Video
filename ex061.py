# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('-=-'*5, 'Gerador de PA', '-=-'*5)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
n = 0
c = 0
while c < 10:
    n = termo + (razao * c)
    c = c + 1
    print('{}'.format(n), end=' -> ')
print('FIM')
