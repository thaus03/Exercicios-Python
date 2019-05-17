# Refaça o DESAFIO 035 dos triangulo, acrescentando o recurso de mostrar que tipo de triangulo será formado:
# - Equilátero: Todos os lados iguais
# - Isósceles: Dois lados iguais
# - Escaleno: todos os lados diferentes

# | b - c | < a < b + c
# | a - c | < b < a + c
# | a - b | < c < a + b
from math import fabs
cores = {
    'limpa': '\033[m',
    'lilas': '\033[4;35m',
    'pretoebranco': '\033[7;30m',
    'vermelho': '\033[31m'
}
r1 = int(input('{}Digite a medida da primeira reta:{} '.format(cores['lilas'], cores['limpa'])))
r2 = int(input('Digite a medida da segunda reta: '))
r3 = int(input('Digite a medida da terceira reta: '))
if fabs(r2 - r3) < r1 < (r2 + r3) and fabs(r1 - r3) < r2 < (r1 + r3) and fabs(r1 - r2) < r3 < (r1 + r2):
    print('{}Triangulo Possível{}'.format(cores['pretoebranco'], cores['limpa']))
    if r1 == r2 == r3:
        print('Triangulo Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Triangulo Isósceles')
    else:
        print('Triangulo Escaleno')
else:
    print('{}Não é possível formar um triangulo{}'.format(cores['vermelho'], cores['limpa']))
print('--FIM--')
