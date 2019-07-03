# Desafio 079
# Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os numa lista.
# Caso o número já exista lá dentro ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = list()
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Valor duplicado. Não adicionado')
    ctr = str(input('Deseja continuar [S/N]? ')).upper()[0]
    if ctr == 'N':
        print('Programa encerrado!')
        break
lista.sort()
print(f'Os valores únicos digitados são: {lista}')
