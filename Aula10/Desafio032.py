# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
num3 = int(input('Digite um ano: '))
if num3 % 4 == 0:
    print('Ano Bissexto')
else:
    if num3 % 400 == 0:
        print('Ano bissexto')
    else:
        print('Não é um ano bissexto')
print('--FIM--')