
# Listas
lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']

# Adiciona um elemento no final da lista
print(f'Lista inicial: {lanche}')

lanche.append('Cookie')
print(f'Lista após o append: {lanche}')

# Adicionar item na posição N
lanche.insert(0, 'Cachorro-quente')
print(f'Lista após o insert: {lanche}')

## Apagar elementos
#
#
    # Apagam pelo índice
del lanche[3]
lanche.pop(3)
    # Apaga pelo nome do elemento
lanche.remove('Cachorro-quente')
print(f'Lista após os deletes: {lanche}')
    # Apaga o último elemento da lista
lanche.pop()
print(f'Lista após os deletes: {lanche}')

# Criar listas através de ranges

valores = list(range(4, 11))
print(valores)

valores2 = [8, 2, 5, 4, 9, 3, 0]

valores2.sort()
print(valores2)
valores2.sort(reverse=True)
print(valores2)
print(len(valores2))

valores3 = list()
valores3.append(5)
valores3.append(9)
valores3.append(4)

for c, v in enumerate(valores3):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

# Uma lista receber uma cópia dos dados da outra

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
