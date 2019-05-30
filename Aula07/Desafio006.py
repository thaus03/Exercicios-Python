# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from math import sqrt
num = int(input('Digite um número: '))
print(f'\033[4;33;40mO dobro é {num * 2}')
print(f'\033[7;41mO triplo é {num * 3}')
print(f'\033[1;46mA raiz quadrada vale {int(sqrt(num))}')
