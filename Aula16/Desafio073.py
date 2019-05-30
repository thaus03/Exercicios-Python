# Desafio 073
# Crie uma tupla peenchida com os 20 primeiros colocados do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#
# A) Apenas os 5 primeiros colocados
# B) Os últimos 4 colocado na tabela.
# C) Uma lista com os times em ordem alfabética
# D) Em que posição na tabela está o time da Chapecoense.

BrasileiroA = ('Palmeiras', 'Atlético-MG', 'Corinthians', 'São Paulo', 'Santos', 'Flamengo', 'Internacional', 'Bahia',
               'Ceará', 'Goiás', 'Botafogo', 'Athletico-PR', 'Chapeconese', 'Fortaleza', 'Fluminense', 'Cruzeiro',
               'CSA', 'Grêmio', 'Avaí', 'Vasco')

print('*' * 40)
print('{:^40}'.format('TABELA DO BRASILEIRÃO 2019'))
print('*' * 40)

print('\033[1;32mOs 5 primeiros colocados:\033[m')
print(f'{BrasileiroA[:5]}')

print('\n\033[1;31mOs últimos 4 colocados na tabela:\033[m ')
print(f'{BrasileiroA[-4:]}')

print('\n\033[1;34mA lista dos times em ordem alfabética:\033[m ')
print(f'{sorted(BrasileiroA)}')

print(f'\n\033[7;31mO Flamengo está em {BrasileiroA.index("Flamengo") + 1}º lugar.\033[m')

