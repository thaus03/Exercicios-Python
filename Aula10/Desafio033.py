# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.[VER RESOLUÇÃO]

# num4 = int(input('Digite o primeiro número: '))
# num5 = int(input('Digite o segundo número: '))
# num6 = int(input('Digite o terceiro número: '))
# # Verificando quem é menor
# menor = num4
# if num5 < num4 and num5 < num6:
#     menor = num5
# if num6 < num4 and num6 < num5:
#     menor = num6
# print('O menor número é o {}.'.format(menor))
# # Verificando quem é maior
# maior = num4
# if num5 > num4 and num5 > num6:
#     maior = num5
# if num6 > num4 and num6 > num5:
#     maior = num6
# print('O maior número é o {}.'.format(maior))
# print('--FIM--')

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite o ultimo numero: '))

if num1 > num2 and num1 > num3:
    print(f'O número {num1} é o maior')
else:
    if num2 >num1 and num2 > num3:
        print(f'O número {num2} é o maior')
    else:
        print(f'O número {num3} é o maior')
if num1 < num2 and num1 < num3:
    print(f'O número {num1} é o menor')
else:
    if num2 < num1 and num2 < num3:
        print(f'O número {num2} é o menor')
    else:
        print(f'O número {num3} é o menor')
print('--FIM--')
