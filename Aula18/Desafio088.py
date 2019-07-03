# Desafio 088
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import sample
from time import sleep
jogo = []
qt = int(input('Informe quantos palpites você quer que sejam gerados: '))
for l in range(0, qt):
    jogo.append(sample(range(1, 60), k=6))
    jogo[l].sort()

print('*' * 35)
print('** MEGA-SENA GERADOR DE PALPITES **')
print('*' * 35)
for p in range(0, qt):
    print(f'Jogo {p+1}: { jogo[p] }')
    sleep(1)
print('-='*5, '< BOA SORTE >', '=-'*5)
    # jogo[l][c].append(sample(range(1, 60), k=6))


# ** SOLUÇÃO DO PROFESSOR **

from random import randint
lista = list()
jogos = list()
print('-'*30)
print('      JOGA NA MEGA SENA       ')
print('-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3,f' SORTEANDO {quant} JOGOS', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')


