# Desafio 078
# Faça um programa que leia 5 valores númericos e guarde em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


lista = list()
for idc in range(0, 5, 1):
    num = int(input(f'Digite o número na posição {idc+1}: '))
    lista.append(num)
print(lista)

print(f'O Maior valor na lista é o {max(lista)} que está na(s) posição(ões) ', end='')
for c, item in enumerate(lista):
    if item == max(lista):
        print(c + 1, end=' ... ')
print(f'\nO Menor valor na lista é o {min(lista)} que está na(s) posição(ões) ',   end='')
for c, item in enumerate(lista):
    if item == min(lista):
        print(c + 1, end=' ... ')
