# Refaça o desafio 009 mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

# Desafio 09: Faça um programa que leia um númeor inteiro qualquer e mostre na tela a sua tabuada
# n6 = int(input('Digite um número inteiro: '))
# print('*' * 32)
# print('*'*5, 'Tabuada do número ', n6, '*'*5)
# print('*' * 32)
# print('{} * 1 = {}'.format(n6, n6*1))
# print('{} * 2 = {}'.format(n6, n6*2))
# print('{} * 3 = {}'.format(n6, n6*3))
# print('{} * 4 = {}'.format(n6, n6*4))
# print('{} * 5 = {}'.format(n6, n6*5))
# print('{} * 6 = {}'.format(n6, n6*6))
# print('{} * 7 = {}'.format(n6, n6*7))
# print('{} * 8 = {}'.format(n6, n6*8))
# print('{} * 9 = {}'.format(n6, n6*9))
# print('{} * 10 = {}'.format(n6, n6*10))
# print('*' * 32)

n = int(input('Digite um número: '))

print(' ##### Tabuada do número {} #####'.format(n))
for i in range(0, 11):
    print('{} * {} = {}'.format(n, i, n * i))
print('*' * 32)
print('-- FIM --')
