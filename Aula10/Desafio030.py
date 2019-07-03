# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

# num1 = int(input('Digite um número inteiro: '))
# if num1 % 2 == 0:
#     print('O número {} é um número PAR'.format(num1))
# else:
#     print('O número {} é um número ÍMPAR'.format(num1))
# print('--FIM--')

numero = int(input('\033[34mDigite um número inteiro:\033[m '))
print(f'O número {numero} é PAR' if numero % 2 == 0 else f'O número {numero} é ÍMPAR')
print('--FIM--')
