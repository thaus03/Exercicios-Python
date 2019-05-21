# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos númeors fora digitados e qual foi a soma entre eles.(Desconsiderando o flag)

i = 0
cont = 0
soma = 0
while i != 999:
    i = int(input('\033[7;31;40mDigite um número:\033[m '))
    if i != 999:
        soma += i
        cont += 1
print('Foram digitados {} números e a soma deles foi {}'.format(cont, soma))
