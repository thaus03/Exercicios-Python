# Desenvolva uma logica que leia o peso e a altura de uma pessoa,
# calcule o IMC e mostre seu status, de acordo com a tabela abaixo.
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

# IMC = peso / altura²

from math import pow
peso = float(input('Informe o seu peso em Kg: '))
alt = float(input('Informe sua altura em m: '))
imc = peso / pow(alt, 2)
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Parabéns! Você está em seu peso ideal!')
elif 25 <= imc < 30:
    print('Maneira na gordurinha, você está com sobrepeso')
elif 30 <= imc < 40:
    print('Opa! Hora de procurar uma academia, você está com obesidade.')
else:
    print('Hora de procurar reeducação alimentar, seu grau é de obesidade mórdida :/ ')

print("""" INFORMAÇÕES:
    IMC: {}""".format(imc))
print('--FIM--')