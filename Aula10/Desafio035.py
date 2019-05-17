# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# | b - c | < a < b + c
# | a - c | < b < a + c
# | a - b | < c < a + b
from math import fabs
r1 = int(input('Digite a medida da primeira reta: '))
r2 = int(input('Digite a medida da segunda reta: '))
r3 = int(input('Digite a medida da terceira reta: '))
if fabs(r2 - r3) < r1 < (r2 + r3) and fabs(r1 - r3) < r2 < (r1 + r3) and fabs(r1 - r2) < r3 < (r1 + r2):
    print('Triangulo Possível')
else:
    print('Não é possível formar um triangulo')
print('--FIM--')