# Faça um programa que calcule a soma entre todos os número ímpares que são multiplos de 3 e que se encontram no intervalo de 1 e 500

s = 0
for i in range(0, 500, 3):
    s += i
print(s)
