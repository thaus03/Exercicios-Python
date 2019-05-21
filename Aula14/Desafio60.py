# Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5 * 4 * 3 * 2 *1 = 120

n1 = 1
fat = int(input('\033[1;46mDigite um número:\033[m '))
while fat != 1:
    n1 = n1 * fat
    fat -= 1
print(n1)
