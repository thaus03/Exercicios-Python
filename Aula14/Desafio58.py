# Melhore o jogo do DESAFIO 028 onde o computador vai pensar em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.l

import random
palpites = 1
pc = random.randint(0, 10)
print('\033[1;34mO computador já pensou em um número!\033[m')
user = int(input('\033[4mDigite um número entre 0 e 10: \033[m'))
while pc != user:
    if pc != user:
        print('Não foi dessa vez, tente novamente.')
        palpites += 1
        user = int(input('Digite novamente o um número : '))
    else:
        print('Parabéns você acertou o número')
print('Foram necessários {} palpites até você acertar.'.format(palpites))
print('O computador escolheu o número {} e você o {}'.format(pc, user))
print('--FIM--')
