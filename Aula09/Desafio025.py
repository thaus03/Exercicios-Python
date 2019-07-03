# Crie um programa que leia o nome da pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite o seu nome: ')).strip()
print(f'O nome {nome.title()} possui a palavra "SILVA" em seu nome? {"SILVA" in nome.upper().split()}')
