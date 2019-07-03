# Desafio 082
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados respectivamente.
#
# Ao final, mostre o conteúdo das três listas geradas.

lista = list()
lista_par = list()
lista_impar = list()

while True:
    num = int(input('\033[7;30mDigite um número:\033[m '))
    lista.append(num)
    ctrl = str(input('Deseja continuar [S/N]? ')).upper()[0]
    # Break
    if ctrl == 'N':
        break

for item in lista:
    if item % 2 == 0:
        lista_par.append(item)
    else:
        lista_impar.append(item)
print(lista)
print(f'A lista com os números pares é: {lista_par}')
print(f'A lista com os números ímpares é: {lista_impar}')
