# Desafio 080
# Crie um programa onde o usuário possa digitar 5 valores númericos e cadastre-os em uma lista,
# já na posição correta de inserção (Sem UTILIZAR o sort()).
# No final, mostre a lista ordenada na tela.


lista = list()
for i in range(0, 5, 1):
    num = int(input(f'Digite o {i}º valor: '))
    if len(lista) == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
print(f'Os valores digitado em ORDEM CRESCENTE são {lista}')
