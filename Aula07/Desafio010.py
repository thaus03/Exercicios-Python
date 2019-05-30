# Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere:
# US$ 1,00 = R$3,27

dinheiro = float(input('Informe quanto dinheiro você possui: '))
print(f'Você pode comprar \033[32m{dinheiro//3.27}\033[m dólares')
