# Faça um programa que leia um ângulo qualquer e moste na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
num = float(input('Infome o valor do ângulo: '))
print(f'\033[30;41mO valor do seno é {sin(radians(num)):.2f}\033[m')
print(f'\033[30;42mO valor do cossenho é {cos(radians(num)):.2f}\033[m')
print(f'\033[30;43mO valor da tangente é {tan(radians(num)):.2f}\033[m')
