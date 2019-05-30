# Tupla
# lanche = ()
# Lista
# lanche = []
# Dicionário
# lanche = {}

lanche = 'Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata-frita'

print(lanche)
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[:3])
print(lanche[2:])
print(lanche[1::-1])

# TUPLAS SÃO IMUTÁVEIS

# lanche[1] = 'Refrigerante'
# print(lanche[1])
print('#' * 40)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')

print('#' * 40)
print(len(lanche))

print('#' * 40)
for cont in range(0, len(lanche)):
    print(lanche[cont])


print('#' * 40)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida}l na posição {pos}')
