# Desafio 081
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados
# B) A lista de valores, ordenada de forma DECRESCENTE
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = list()
while True:
    num = int(input('\033[1;33mDigite um número:\033[m '))
    lista.append(num)
    ctrl = str(input('Deseja continua [S/N]? ')).upper()[0]
    if ctrl == 'N':
        break
print('*' * 30)
print(f'Foram adicionados {len(lista)} números na lista.')
lista.sort(reverse=True)
print(f'A lista ordenada em ORDEM DECRESCENTE é {lista}')
if 5 in lista:
    print(f'O número 5 apareceu {lista.count(5)} vezes na lista.')
else:
    print(f'O número 5 não foi digitado nenhuma vez.')
print('Programa encerrado com sucesso.')
