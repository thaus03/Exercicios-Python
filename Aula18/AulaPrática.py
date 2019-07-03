teste = list()
teste.append('Igor')
teste.append('28')
galera = list()
galera.append(teste[:])
teste[0] = 'Renata'
teste[1] = 29
galera.append(teste[:])
print(galera)



galera = [['Geovanna',21], ['Matheus',23], ['Cristina',61], ['Gloria',67]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])

for p in galera:
    print(f'O nome é {p[0]}')


galera = list()
dado = list()
tot_maior = tot_menor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'O {p[0]} é maior de idade')
        tot_maior += 1
    else:
        print(f'O {p[0]} é menor de idade')
        tot_menor += 1
print(f'Temos {tot_maior} maiores e {tot_menor} menores de idade')
