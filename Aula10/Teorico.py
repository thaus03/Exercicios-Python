# Curso Python #10 - Condições (Parte 1)

# Modo 1

tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')
# Modo 2
tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo <=3 else 'Carro velho')
print('--FIM--')