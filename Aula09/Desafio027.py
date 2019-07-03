# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
# Ex: Ana Maria de Souza
# primeiro: Ana
# ultimo: Souza

nome = str(input('Digite o nome completo: '))
print(f'Primeiro: {nome.split()[0].capitalize()}')
print(f'Ultimo: {nome.split()[-1].capitalize()}')
print('--FIM--')
