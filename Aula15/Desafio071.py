
# Desafio 071
# Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio pergunte ao usuário qual será o valor
# a ser sacado (número inteiro) e o programa vai informa quantas cédulas de cada valor serão entregues.
#
# OBS: Considere que os caixa possui cédulas de R$50, R$20, R$10 e R$1.

saque = notac = notav = notad = notau = 0
print('$' * 30)
print('{:^30}'.format('THAUS BANK'))
print('$' * 30)
print('')
print('Notas disponíveis: R$50, R$20, R$10 e R$1')
saque = int(input('Quanto deseja sacar? '))
notac = saque // 50
notav = (saque % 50) // 20
notad = ((saque % 50) % 20) // 10
notau = (((saque % 50) % 20) % 10) // 1


print('='* 30)
print('{:^30}'.format('TOTAL DE CEDULAS'))
print('='* 30)
print(f'Total de {notac} cédulas de R$ 50')
print(f'Total de {notav} cédulas de R$ 20')
print(f'Total de {notad} cédulas de R$ 10')
print(f'Total de {notau} cédulas de R$ 1')
print('')
print('\033[7;30mObrigado e volte sempre!\033[m')
