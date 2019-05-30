# Desafio 072
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero a vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso. (Fazer a verificação)

numero = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quize','dezesseis','dezesete','dezoito','dezenove','vinte'
num = int(input('Informe um número de 0 à 20: '))
while num > 20 or num < 0:
    num = int(input('Número incorreto, por favor, digite de 0 a 20: '))
print(f'O número digitado foi o \033[1;32m{numero[num]}\033[m.')

