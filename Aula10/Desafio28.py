# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou
# perdeu.

import random
pc = random.randint(0,5)
print('\033[1;34mO computador já pensou em um número!')
user = int(input('Digite um número entre 0 e 5: \033[m'))
if pc == user:
    print('Parabéns você acertou o número')
else:
    print('Não foi dessa vez, tente novamente.')
# print('O computador escolheu o número {} e você o {}'.format(pc,user))
print('--FIM--')
