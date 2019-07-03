# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado.

dist = float(input('Informe quantos Km foram percorridos: '))
dias = int(input('Informe quantos dias o carro foi alugado: '))

print(f'O preço a pagar é R${(dist*0.15)+(60*dias):.2f}')
