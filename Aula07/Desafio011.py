# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input('Digite a largura da parede em metros (m): '))
altura = float(input('Digite a altura da parede em metros (m): '))
print(f'A parede possui {largura*altura}m² e para pintá-la são necessários {int((largura*altura)//2)} litros de tinta')
