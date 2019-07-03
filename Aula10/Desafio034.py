# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores aR$ 1.250,00, calcule um aumento de 10%.
# Para inferiores ou iguais, o aumento é de 15%.

# sal = int(input('\033[7;30mDigite o salário do funcionário:\033[m '))
# if sal <= 1250:
#     aumento = ((sal * 15) / 100)
# else:
#     aumento = ((sal * 10) / 100)
#
# print('\033[7;30;46m O aumento para o salário informado é de R$ {:.2f}'.format(aumento))
# print('--FIM--')

salario = float(input('Qual o salário do funcionario (R$)? '))
print(f'O valor do aumento será de R${salario * 10 /100:.2f}' if salario > 1250 else f'O valor do aumento será de R${salario * 15 / 100:.2f}')
