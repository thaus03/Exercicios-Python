# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.


from datetime import datetime
maiores = 0
menores = 0
anoAtual = datetime.now().year
for i in range(0, 7):
    anoNasc = int(input('Digite o ano de nascimento: '))
    if anoAtual - anoNasc >= 18:
        maiores += 1
    else:
        menores +=1
print('O Total de {} pessoas já são maiores e {} pessoas não atingiram a maioridade'.format(maiores, menores))


