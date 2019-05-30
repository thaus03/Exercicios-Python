# Desafio 066
# Crie um programa que leia vários números inteiros pelo teclado.
# O Programa só vai para quando o usuário digitar o valor 999, que é a condição de parada.
# No final mostre quantos números foram digitados e qual foi a soma entre eles (Desconsiderando o flag)


cont = soma = 0
while True:
    num = int(input('\033[1;41mDigite um número inteiro (Digite 999 para parar):\033[m '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Foram digitados {cont} e a soma deles é {soma}.')

# OBS: O if deve ser colocado antes do contador e da soma, para que o valor 999 não seja contado.
