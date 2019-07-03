# Desafio 084
# Faça um programa que leia o nome e o peso de várias pessoas, guardando tudo em uma lista. No final, moste:
# A) Quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas
# C) Uma listagem com as pessoas mais leves

dado = list()
pessoas = list()
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    ctrl = str(input('Deseja continuar [S/N]? '))[0]
    if ctrl in 'Nn':
        break
print('#' * 30)
print(f'\033[31mForam cadastradas {len(pessoas)} pessoas\033[m')
# print(pessoas)
"""
    ** Buscando o maior peso
    - Construção de dois loops, o primeiro procura o maior peso e a variável "maior" recebe ele. O segundo loop pesquisa
    na lista quais os nomes correspondentes ao maior peso.      """

for p in pessoas:
    if p[1] > maior:
        maior = p[1]
print(f'O maior peso é {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
"""
    ** Buscando o menor peso
    - Construção de dois loops, o primeiro procura o menor peso e a variável "menor" recebe ele. O segundo loop pesquisa
    na lista quais os nomes correspondentes ao menor peso.
    Porém nessa busca o if recebe uma condição a mais, onde a lógica para achar o menor número é um pouco mais complexa.
"""
for c, p in enumerate(pessoas):
    if c == 0:
        menor = p[1]
    elif p[1] < menor:
        menor = p[1]
print(f'\n\033[33mO menor peso é {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]\033[m', end=' ')

