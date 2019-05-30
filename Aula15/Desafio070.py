# Desafio 070
# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai contunuar.
# No final, mostre:
#
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000
# C) Qual é o nome do produto mais barato.

print('~' * 30)
print('{:^30}'.format('MERCADO SUPER BARATÃO'))
print('~' * 30)
nome = prodcheapname = choice = ''
preco = tot = cont = prodmil = prodcheap = 0

while True:
    nome = str(input('Informe o nome do produto: '))
    preco = float(input('Informe o preço do produto: '))
    cont += 1
    tot += preco

    if preco > 1000:
        prodmil += 1

    if cont == 1:
        prodcheapname = nome
        prodcheap = preco

    if preco < prodcheap and cont > 1:
        prodcheapname = nome

    choice = str(input('Deseja continuar ? [S/N]')).strip().upper()[0]
    if choice == 'N':
        break
print('~' * 30)
print(f'Total da lista ({cont} produtos)')
print(f'O total gasto na compra é de R${tot:.2f}')
print(f'{prodmil} produtos custam mais de R$1000')
print(f'{prodcheapname} é o produto mais barato')
