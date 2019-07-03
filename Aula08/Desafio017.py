# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

from math import hypot
co = float(input('Informe o valor do Cateto Oposto: '))
ca = float(input('Informe o valor do Cateto Adjacente: '))
print(f'\033[4;33mO valor da Hipotenusa para os catetos informados é {hypot(co, ca)}.')
