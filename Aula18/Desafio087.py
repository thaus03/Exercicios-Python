# Desafio  087
# Aprimore o desafio anterior mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

soma_pares = soma_coluna = maior_linha = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
print('#' * 40)
for p in matriz:
    print(f'[ {p[0]:^4} ]    [ {p[1]:^4} ]    [ {p[2]:^4}] ')

print('~'*32)
print('** Adicionando o Desafio 087  **')
print('~'*32)
for l in range(0, 3):
    soma_coluna += matriz[l][2]
    maior_linha = max(matriz[1])
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
print(f'\033[31mA soma dos números pares é {soma_pares}\033[m')
print(f'\033[32mA soma dos números da terceira coluna é {soma_coluna}\033[m')
print(f'\033[33mO maior valor da segunda linha é {maior_linha}\033[m')

