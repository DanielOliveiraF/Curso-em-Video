# Crie uma tupla preenchida com os 20 primeiros colocados da
# Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
         'Flamengo', 'Vasco da Gama', 'Chapecoense', 'Atlético-MG', 'Botafogo',
         'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport',
         'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-='*20)
print(f'Lista de times do Brasileirão 2017: {times}')
print('-='*20)
print(f'Os 5 primeiros são {times[0:5]}')
print('-='*20)
print(f'Os 4 último são {times[-4:]}')
print('-='*20)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('-='*20)
print(f'A Chapecoense está na {times.index("Chapecoense") + 1}ª posição.')