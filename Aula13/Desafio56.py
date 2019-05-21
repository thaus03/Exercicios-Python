# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos

media = 0
homem_velho = ''
idade_hv = 0
idade_mulher = 0
for i in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(i)))
    idade = int(input('Digite a idade dessa pessoa: '))
    sexo = str(input('Digite o sexo desta pessoa[M ou F]: ')).upper()
    media += idade
    if idade > idade_hv and sexo == 'M':
        homem_velho = nome
    if idade < 20 and sexo == 'F':
        idade_mulher += 1
media = media / 4
print('#' * 20)
print('A média de idade do grupo é {}'.format(media))
print('O nome do homem mais velho é {}.'.format(homem_velho))
print('{} mulher(es) tem menos de 20 anos.'.format(idade_mulher))
print('--FIM--')
