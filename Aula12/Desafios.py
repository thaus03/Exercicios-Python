# Crie um programa que faça o computador jogar Jokenpô com você
from random import choice
print('='*20)
print('VAMOS JOGAR JOKENPÔ')
print('='*20)
mychoice = str(input("""As opções possiveis são: (Pedra, Papel ou Tesoura)
Digite sua escolha, prometo que não vou olhar! """)).upper()
print('JOOOO....KEEEEN....PÔÔÔO....')
pcchoice = choice(['Pedra', 'Papel', 'Tesoura']).upper()

print("""Sua escolha foi {}
Minha escolha foi {}""".format(mychoice, pcchoice))

if (mychoice == 'PEDRA' and pcchoice == 'TESOURA') or (mychoice == 'TESOURA' and pcchoice == 'PAPEL') or (mychoice == 'PAPEL' and pcchoice == 'PEDRA'):
    print('Parabéns! Você me ganhou :) ')
elif (mychoice == 'TESOURA' and pcchoice == 'PEDRA') or (mychoice == 'PAPEL' and pcchoice == 'TESOURA') or (mychoice == 'PEDRA' and pcchoice == 'PAPEL'):
    print('HAHA! Dessa vez eu que ganhei!')
elif mychoice == pcchoice:
    print('Não tem jeito, dessa vez foi um empate!')
print('Muito bom jogar com você')
print('--FIM--')

