# Desafio 089
# Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

from statistics import median
boletim = list()
aluno = list()
nota = list()
while True:
    aluno.append(str(input('Informe o nome do aluno: ')))
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota 2: ')))
    aluno.append(nota[:])
    aluno.append(median(nota))
    boletim.append(aluno[:])
    aluno.clear()
    nota.clear()
    ctrl = str(input('Quer continuar [S/N]? '))[0]
    if ctrl in 'Nn':
        break
print('*'*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*25)
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-'*25)
while True:
    ctrl = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if ctrl == 999:
        break
    print(f'Notas de {boletim[ctrl][0]} são {boletim[ctrl][1]}')
    print('='*55)
print('Finalizando...')
print('<<<< VOLTE SEMPRE >>>>')



# print(boletim)
# print(aluno)
# print(nota)

# test = [['Igor', [8.0, 9.0], 8.5], ['Renata', [5.0, 7.0], 6.0]]
# print(test[0][0])
# for i, a in enumerate(test):
#     print(a[0])
