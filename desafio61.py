# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('-=-'*5, 'Gerador de PA', '-=-'*5)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ->'.format(termo), end=' ')
    termo = termo + razao
    cont = cont + 1
print('FIM')