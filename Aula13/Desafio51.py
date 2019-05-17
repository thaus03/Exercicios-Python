# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa progressão.

# DEFINIÇÃO: Uma progressão aritmética (abreviadamente, P. A.) é uma sequência numérica em que cada termo, a partir do segundo,
# é igual à soma do termo anterior com uma constante r. O número r é chamado de razão ou diferença comum da progressão aritmética.

# FÓRMULA: O n-ésimo termo de uma progressão aritmética, denotado por N, pode ser obtido por meio da fórmula:
# em que:
#
#     p  é o primeiro termo;
#     r é a razão.

p = int(input('Digite o primeiro termo de sua Progressão Aritimética: '))
r = int(input('Agora, digite a razão ou diferença comum: '))
s = 0
for i in range(p, p + (11 - 1) * r, r):
    print(i)
print()
