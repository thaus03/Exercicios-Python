# Crie um programa que leia um número Real qualquer e mostr na tela a sua porção inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6

from math import trunc
num = float(input('Digite um número:'))
print(f'\033[4;36mO número {num} tem a parte inteira {trunc(num)}.\033[m')
