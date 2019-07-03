# Desafio 086
# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

# matriz = [[], [], []]
# '''
#     1) Cada for insere um conjunto de 3 números
#     2) Cada conjunto de 3 números é inserido em uma posição da lista
#     3) No final a lista é montada no formato da matriz
# '''
# for i in range(0, 3):
#     pos = int(input(f'Digite o número na posição [0, {i}]: '))
#     matriz[0].append(pos)
# for i in range(0, 3):
#     pos = int(input(f'Digite o número na posição [1, {i}]: '))
#     matriz[1].append(pos)
# for i in range(0, 3):
#     pos = int(input(f'Digite o número na posição [2, {i}]: '))
#     matriz[2].append(pos)
#
# print('#' * 40)
# for p in matriz:
#     print(f'[ {p[0]:^4} ]    [ {p[1]:^4} ]    [ {p[2]:^4}] ')

'''
------------------------------------------------------------------------------------

Solução do professor
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()


