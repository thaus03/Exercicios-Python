# Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o

s = 0
for i in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
print('A soma dos números pares é {}'.format(s))
print('-- FIM --')
