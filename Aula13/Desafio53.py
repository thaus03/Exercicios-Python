# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
# Ex: APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA BOLO
# ANOTARAM A DATA DA MARATONA

# frase = str(input('Digite a frase: ')).upper().split()
# tal = ''
# print('O TAMANHO DA STRING É {}'.format(len(frase)))
# for i in range(0, len(frase)):
#     tal += frase[i]
# print(tal, end='')
# print('\n')
# print(frase[0][0])
# # letra = tal.partition()
# #print(letra)
#
# for j in range(len(frase)-1, -1, -1):
#     print(frase[j], end='')


# SOLUÇÃO DO PROFESSOR

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(inverso, junto)
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

# SOLUÇÃO MAIS SIMPLES

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
# inverso = ''
inverso = junto[::-1]
# for letra in range(len(junto) - 1, -1, -1):
#     inverso += junto[letra]
print(inverso, junto)
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')




