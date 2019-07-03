# Crie um programa que leia o nome completo de uma pessoa e mostre:
    # O nome com todas as letras maiúsculas
    # O nome com todas minusculas
    # Quantas letras (sem considerar espaços)
    # Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print(f'\033[1;31mO seu nome em MAIÚSCULO é \033[m{nome.upper()}')
print(f'O seu nome em MINÚSCULO é {nome.lower()}')
print(f'Ele possui {len("".join(nome.split()))} letras')
print(f'Ele possui {len(nome.replace(" ",""))} letras')
print(f'O seu primeiro nome é {nome.split()[0].capitalize()} e ele possui {len(nome.split()[0])} letras')
