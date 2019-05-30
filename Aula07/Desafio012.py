# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Digite o valor do produto R$ '))
print(f'O novo valor deste produto é R${produto - ((produto*5)/100)}')
