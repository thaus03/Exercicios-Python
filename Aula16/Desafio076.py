# Desafio 076
# Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços na sequencia.
# No final, mostre uma listagem de preços organizando os dados em forma tabular.

print('=' * 40)
print('{:^40}'.format('Listagem de Preços'))
print('=' * 40)

produtos = ('Caneca', 20, 'Mouse', 40, 'Bombom', 17,'Notebook',2315)
for n in range(0, len(produtos), 2):
    print(f'{produtos[n]:.<30} R${produtos[n+1] :>7.2f}')
print('=' * 40)
