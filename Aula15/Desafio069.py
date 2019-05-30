# Desafio 069
# Crie um programa que leia a idade e o sexo de vários programas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer continuar. No final mostre:
#
# A) Quantas pessoas tem mais de 18.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

idade = maisdezoito = homens = mulher = 0
sexo = choice = ''

while True:
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o sexo [M/F]')).strip().upper()[0]
    if idade > 18:
        maisdezoito += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    choice = str(input('Deseja cadastrar mais pessoas? [S/N] ')).upper().strip()[0]
    if choice == 'N':
        break
print('#' * 30)
print('Dentre a população cadastrada: ')
print(f'{maisdezoito} pessoas tem mais de 18 anos')
print(f'{homens} homens foram cadastrados.')
print(f'{mulher} mulheres com menos de 20 anos')
