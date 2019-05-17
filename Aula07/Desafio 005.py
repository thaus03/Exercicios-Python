# FUP que leia um número inteiro e moste na tela o seu sucessor e seu antecessor.

n1 = int(input('Digite um número inteiro: '))
print('O antecessor desse número é {}, e o sucessor é {}.'.format(n1-1, n1+1))

# Crie um algoritmo que leia um número e mostre seu dobro, seu triplo e sua raiz quadrada

n2 = float(input('Digite um número: '))
print('O dobro desse número é {}, o triplo é {} e sua raiz quadrada vale {}'.format(n2*2, n2*3, n2**0.5))

# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média

n3 = float(input('Digite a primera nota: '))
n4 = float(input('Digite a segunda nota: '))
print('A média do aluno é {}.'.format((n3+n4)/2))

# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros

n5 = float(input('Digite um valor em Metros(m):' ))
print('O valor em centímetros é {} e em milímetros é {}.'.format(n5*100, n5*1000))

# FUP que leia um númeor inteiro qualquer e mostre na tela a sua tabuada

n6 = int(input('Digite um número inteiro: '))
print('*' * 32)
print('*'*5, 'Tabuada do número ', n6, '*'*5)
print('*' * 32)
print('{} * 1 = {}'.format(n6, n6*1))
print('{} * 2 = {}'.format(n6, n6*2))
print('{} * 3 = {}'.format(n6, n6*3))
print('{} * 4 = {}'.format(n6, n6*4))
print('{} * 5 = {}'.format(n6, n6*5))
print('{} * 6 = {}'.format(n6, n6*6))
print('{} * 7 = {}'.format(n6, n6*7))
print('{} * 8 = {}'.format(n6, n6*8))
print('{} * 9 = {}'.format(n6, n6*9))
print('{} * 10 = {}'.format(n6, n6*10))
print('*' * 32)
# FUP que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1,00 = R$3,27

n7 = float(input('Digite quanto dinheiro você tem: '))
print('O Atual valor do Dólar é US$1,00 = R$3,27')
print('Logo você poderá comprar {} Dólares'.format(int(n7//3.27)))

# FUP que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para
# pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

n8 = float(input('Digite o valor da altura da parede em m: '))
n9 = float(input('Digite o valor da largura da parede em m: '))
print('A área desta parede é {}m² e para pinta-la é necessário {} litros de tinta'.format(n8*n9, int((n8*n9)//2)))

# FUP que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

n10 = float(input('Digite o preço do produto: '))
print('Parabéns! Você ganhou 5% de desconto, o novo valor para o seu produto é {:.2f}'.format(n10-(n10*0.05)))

# FUP que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

n11 = float(input('Digite o valor do salário: '))
print('O valor do salário com 15% de aumento é: R$ {:.2f}'.format(n11+(n11*0.15)))
