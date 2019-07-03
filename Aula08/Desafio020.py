# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos do alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem apresentada.

from random import sample
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))
sorteio = sample([aluno1, aluno2, aluno3, aluno4], k=4)
print(f'\033[4;36mA ordem de apresentação será {sorteio[0]}, {sorteio[1]}, {sorteio[2]} e {sorteio[3]}.\033[m')

