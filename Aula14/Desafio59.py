# Crie um programa que leia dois valores e mostre na tela um menu:
#
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso

menu = 0
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
print('''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
while menu != 5:
    menu = int(input('Digite a opçao: '))
    if menu == 1:
        print('O resultado da soma entre os valores {} e {} é {}.'.format(num1, num2, num1 + num2))
    elif menu == 2:
        print('O produto da multiplicação entre os valores {} e {} é {}.'.format(num1, num2, num1 * num2))
    elif menu == 3:
        if num1 > num2:
            print('O número {} é o maior número.'.format(num1))
        elif num2 > num1:
            print('O número {} é o maior número.'.format(num2))
        else:
            print('Os números são iguais.')
    elif menu == 4:
        num1 = int(input('Digite um novo primeiro valor: '))
        num2 = int(input('Digite um novo segundo valor: '))
    elif menu == 5:
        print('Ok! Encerrando o programa.')
    else:
        print('\033[1;31mINFORME UMA OPÇÃO VALIDA\033[m')
