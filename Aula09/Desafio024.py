# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da cidade: ')).strip()
print(f'\033[7;30mA cidade {cidade.title()} começa com a palavra "Santo"?\033[m {"SANTO" in cidade.upper().split()[0]}')
#Método do Professor
print(f'\033[7;30mA cidade {cidade.title()} começa com a palavra "Santo"?\033[m {cidade[:5].upper() == "SANTO"}')


