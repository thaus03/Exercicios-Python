# Desafio 077
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso você deve mostrar, para cada palavra quais são as suas vogais


palavras = ('ORAEX', 'NOTEBOOK', 'AGUA')

for i in palavras:
    print(f'\nNa palavra {i} temos as vogais ', end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

# ---------------------------------------------------------------
