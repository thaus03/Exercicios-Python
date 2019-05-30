# Desafio004
# Faça um programa que leia algo pelo teclado e depois mostre na tela o seu tipo primitivo e tadas as informações possíveis sobre ele.


var = input('Digite algo pelo teclado: ')
print(f'O tipo primivo é {type(var)}')

print(f'O que foi digitado pode ser um número inteiro? {var.isnumeric()}')
print(f'O que foi digitado é alfabetico? {var.isalpha()}')
print(f'O que foi digitado pode ser um número decimal? {var.isdecimal()}')
print(f'O que foi digitado é alfanumérico? {var.isalnum()}')
print(f'O que foi digitado só pussi espaço? {var.isspace()}')
print(f'O que foi digitado está em minúsculo? {var.islower()}')
print(f'O que foi digitado está em maiúsculo? {var.isupper()}')
print(f'O que foi digitado está captalizado? {var.istitle()}')
