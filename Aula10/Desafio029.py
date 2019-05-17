# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$ 7,00 por cada Km acima da limite.

vel = float(input('Digite a velocidade do carro em Km/h: '))
if vel < 80.0:
    print('\033[32mParabéns! Você está dentro da velocidade permitida.\033[m')
else:
    print('\033[31mOpa! Você passou da velocidade permitida, sua multa é de R${:.0f},00\033[m'.format((vel - 80.0)*7))
print('--FIM--')
