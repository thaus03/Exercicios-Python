# Desafio 067
# Faça um programa que mostra a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

print('#' * 30)
print('{:^30}'.format('TABUADA'))
print('#' * 30)
produto = 0
while True:
    num = int(input('\033[2;30;45mDigite o número que você deseja saber a tabuada:\033[m '))
    if num < 0:
        break
    for i in range(0, 11):
        produto = num * i
        print(f'{num} X {i} = {produto}')
    print('~' * 30)
print('Fim do Programa Tabuada')
