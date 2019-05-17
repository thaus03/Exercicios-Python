# FUP que leia um número real qualquer e mostre na tela a sua porção inteira

import math
n1 = float(input('Digite um número: '))
print('A porção inteira deste número é {}'.format(math.trunc(n1)))

# FUP que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,
# calcule e moste o comprimento da hipotenusa

from math import hypot
n2 = float(input('Digite o valor do cateto oposto: '))
n3 = float(input('Digite o valor do cateto adjacente: '))
print('O valor da hipotenusa é {}'.format(hypot(n2, n3)))

# FUP que leia um angulo qualquer e mostre o valor do seno, cosseno e tangente desse angulo

from math import cos, sin, tan
n4 = float(input('Digite o valor de um angulo: '))
print('O valor do seno é {}, do cosseno é {} e da tangente é {}'.format(sin(n4), cos(n4), tan(n4)))

# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. FUP que ajude ele, lendo o nome deles
# e escrevendo o nome do escolhido.

import random
n5 = str(input('Digite o nome do primeiro aluno: '))
n6 = str(input('Digite o nome do segundo aluno: '))
n7 = str(input('Digite o nome do terceiro aluno: '))
n8 = str(input('Digite o nome do quarto aluno: '))
print('O aluno escolhido foi: {}'.format(random.choice([n5, n6, n7, n8])))

# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. FUP que leia os
# nomes dos quatro alunos e mostre a ordem sorteada.

import random
n5 = str(input('Digite o nome do primeiro aluno: '))
n6 = str(input('Digite o nome do segundo aluno: '))
n7 = str(input('Digite o nome do terceiro aluno: '))
n8 = str(input('Digite o nome do quarto aluno: '))
print('A ordem de apresentação do trabalho é: {}'.format(random.sample([n5, n6, n7, n8], 4)))

# Faça um programa em Python que abra e reproduza o audio de um arquivo MP3

import pygame
pygame.init()
pygame.mixer.music.load('Ring01.wav')
pygame.mixer.music.play()
pygame.event.wait()



