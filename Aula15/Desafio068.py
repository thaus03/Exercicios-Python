# Desafio 068
# Faça um programa que jogue PAR ou ÍMPAR com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
from emoji import emojize
result = mychoice = ''
pcnumber = mynumber = soma = cont = 0
print(emojize('Jogo do Par ou Ímpar, vamos jogar :triangular_flag:'))
while True:
    pcnumber = randint(0, 10)
    mychoice = str(input('Você quer Par ou Ímpar [P/I]? ')).strip().upper()[0]
    mynumber = int(input('Digite seu número [0 - 10]:'))
    soma = mynumber + pcnumber
    # print(pcnumber, mynumber, mychoice)
    if soma % 2 == 0:
        result = 'Par'
    else:
        result = 'Ímpar'
    print(f'Você escolheu o número {mynumber} e o computador escolheu o número  {pcnumber}.')
    print(f'O total deu {soma}, que é um número {result}.')
    if soma % 2 == 0 and mychoice == 'I' or soma % 2 != 0 and mychoice == 'P':
        print(emojize('Não foi dessa vez! GAME OVER! :loudly_crying_face: .'), end='')
        break
    else:
        cont += 1
print(f'Você conquistou {cont} vitórias consecutivas.')
