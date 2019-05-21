# Desafio 57
# Faça um programa que leia o sexo da pessoa, mas só aceite M ou F.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


sexo = ''
while sexo not in ['M', 'F']:
    sexo = str(input('Digite o sexo da pessoa (Use M ou F): '))
