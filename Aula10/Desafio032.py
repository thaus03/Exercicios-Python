# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
# num3 = int(input('Digite um ano: '))
# if num3 % 4 == 0:
#     print('Ano Bissexto')
# else:
#     if num3 % 400 == 0:
#         print('Ano bissexto')
#     else:
#         print('Não é um ano bissexto')
# print('--FIM--')

from datetime import date
ano = int(input('Informe um ano (Digite 0 para ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[32mAno Bissexto\033[m')
else:
    print('\033[31mNão é ano Bissexto\033[m')
print('--FIM--')
