# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.[VER RESOLUÇÃO]

num4 = int(input('Digite o primeiro número: '))
num5 = int(input('Digite o segundo número: '))
num6 = int(input('Digite o terceiro número: '))
# Verificando quem é menor
menor = num4
if num5 < num4 and num5 < num6:
    menor = num5
if num6 < num4 and num6 < num5:
    menor = num6
print('O menor número é o {}.'.format(menor))
# Verificando quem é maior
maior = num4
if num5 > num4 and num5 > num6:
    maior = num5
if num6 > num4 and num6 > num5:
    maior = num6
print('O maior número é o {}.'.format(maior))
print('--FIM--')
