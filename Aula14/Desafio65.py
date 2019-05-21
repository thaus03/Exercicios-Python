# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
# O programa deve perguntar ao usuário se ele quer continuar ou não a digirar valores.
"""
resp = ''
maior = 0
menor = 0
media = 0
cont = 0
numaux = 0
while resp != 'N':
    # Primeira execução
    if resp != 'N':
        num = int(input('\033[7;30mDigite um número:\033[m '))
        cont += 1
        resp = str(input('Deseja continuar? [S/N]')).upper()
        if resp == 'S' and cont == 1 or resp == 'N' and cont == 1:
            maior = menor = numaux = num
        elif resp == 'S' or resp == 'N':
            if maior < num:
                maior = num
            elif num < menor:
                menor = num
            numaux += num
            media = numaux / cont
        else:
            resp = str(input('Deseja continuar? [S/N]')).upper()
print('''
Resp: {}
Maior: {}
Menor: {}
Media: {}
Contador: {}
Numero Auxiliar: {}
'''.format(resp, maior, menor, media, cont, numaux)) """


# RESOLUÇÃO DO PROFESSOR

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print('Voce digitou {} numeros e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
