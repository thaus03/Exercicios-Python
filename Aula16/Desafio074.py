# Desafio 074
# Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla. Depois disso mostre a listagem de números
# gerados e também inque o menor e o maior valor que estão na tupla.

from random import choices
maior = menor = 0
num = (choices(range(1,10),k=5))
print(f'Os números gerados foram {num}. \n')
for i in range(0,len(num)):
    if i == 0:
        maior = menor = num[i]
    if num[i] > maior:
        maior = num[i]
    if num[i] < menor:
        menor = num[i]

print(f'O maior valor da lista é {maior}')
print(f'O menor valor da lista é {menor}\n')

print('#' * 50)
print('\n')
# Solução do professor (Ambas funcionando)

from random import randint
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Eu sorteei os valores {n}')
print(f'O maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')
