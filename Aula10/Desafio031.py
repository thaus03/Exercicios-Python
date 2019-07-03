# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem cobrando R$ 0,50 por Km para viagens até 200 Km e R$ 0,45 para viagens mais longas.

# num2 = int(input('Digite a distancia de sua viagem em Quilometros(Km): '))
# if num2 <= 200:
#     print('Você está pagando a tarifa mais cara. O valor da sua passagem é R$ {:.2f}'.format(num2*0.5))
# else:
#     print('Você está pagando a tarifa mais barata. O valor da sua passagem é R$ {:.2f}'.format(num2*0.45))
# print('--FIM--')

dist = int(input('Digite a distancia (Km): '))
print(f'O valor da passagem é R${dist*0.5:.2f} (Tarifa normal)' if dist <= 200 else f'O valor da passagem é R$ {dist*0.45:.2f} (Tarifa Reduzida)')
