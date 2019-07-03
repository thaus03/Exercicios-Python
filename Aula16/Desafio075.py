# Desafio 075
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os números pares

num = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais  número: ')),
        int(input('Digite o ultimo número: ')))
print(f'Os valores digitados foram {num}')
print(f'O número 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O primeiro valor 3 apareceu na posição {num.index(3) +1} ')
else:
    print('O número 3 não apareceu nenhuma vez')

print(f'Os números pares são ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
    else:
        print('Não há números pares na estrutura.')
