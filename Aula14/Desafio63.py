# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de Fibonacci.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

import emoji
# from emoji import emojise
fib = int(input('Digite o Nézimo valor para a sequencia de Fibonacci: '))
ant1 = 1
ant2 = 1
fib2 = 3

if fib == 0:
    print(' 0 ')
elif fib == 1:
    print(emoji.emojize(' 0 :up-right_arrow: 1 '))
elif fib == 2:
    print(emoji.emojize(' 0 :up-right_arrow: 1 :up-right_arrow: 1 '))
else:
    print(emoji.emojize(' 0 :up-right_arrow: 1 :up-right_arrow: 1'), end='')
    while fib2 <= fib - 1:
        prox = ant1 + ant2
        print(emoji.emojize(' :up-right_arrow: '), prox, end='')
        ant2 = ant1
        ant1 = prox
        fib2 = fib2 + 1
print(emoji.emojize(' :up-right_arrow: FIM'))
