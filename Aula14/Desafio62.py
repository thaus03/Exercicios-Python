### DESAFIO 62
# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostar 0 termos

### DESAFIO 61
# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while

### DESAFIO 51
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa progressão.
# DEFINIÇÃO: Uma progressão aritmética (abreviadamente, P. A.) é uma sequência numérica em que cada termo, a partir do segundo,
# é igual à soma do termo anterior com uma constante r. O número r é chamado de razão ou diferença comum da progressão aritmética.

# FÓRMULA: O n-ésimo termo de uma progressão aritmética, denotado por N, pode ser obtido por meio da fórmula:
# em que:
#
#     p  é o primeiro termo;
#     r é a razão.

'''p = int(input('Digite o primeiro termo de sua Progressão Aritimética: '))
r = int(input('Agora, digite a razão ou diferença comum: '))
s = 0
for i in range(p, p + (11 - 1) * r, r):
    print(i)
print('-- FIM --')'''


'''
p = int(input('Digite o primeiro termo de sua Progressão Aritimética: '))
r = int(input('Agora, digite a razão ou diferença comum: '))
i = 0
while i != 10:
    print(p)
    p = p + r
    i += 1
    if i == 10:
        j = int(input('Gostaria de mostrar mais alguns termos? '))
        if j != 0:
            while i != (10 + j):
                print(p)
                p = p + r
                i += 1
        else:
            print('Saindo do programa...')
print('-- FIM --')'''

# RESOLUÇÃO DO PROFESSOR

p = int(input('Digite o primeiro termo de sua Progressão Aritimética: '))
r = int(input('Agora, digite a razão ou diferença comum: '))
i = 0
total = 0
mais = 10
cont = 1
while mais != 0:
    total += mais
    while i != total:
        print('{} -> '.format(p), end ='')
        p = p + r
        i += 1
    print('PAUSA')
    mais = int(input('\033[7;30mQuantos termos você quer a mais?\033[m '))
print('Progrssão finalizada mostrando {} termos'.format(i))
