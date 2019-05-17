# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual
# será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal

num1 = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num1, bin(num1)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num1, oct(num1)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num1, hex(num1)[2:]))
else:
    print('OPÇÃO INVÁLIDA, POR FAVOR TENTE NOVAMENTE')
print('--FIM--')
