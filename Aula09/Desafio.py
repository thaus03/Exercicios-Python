# FUP que leia o nome completo de uma pessoa e mostre:
    # O nome com todas as letras maiúsculas
    # O nome com todas minusculas
    # Quantas letras (sem considerar espaços)
    # Quantas letras tem o primeiro nome

frase1 = str(input('Digite o seu nome completo: '))
print(frase1.upper())
print(frase1.lower())
print(len(frase1.replace(' ', '')))
print(len(frase1.split()[0]))

#FUP que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. Ex: Digite um número: 1834
# Unidade: 4 Dezena: 3 Centena: 8 Milhar: 1

num1 = int(input('Digite um número de 0 a 9999'))
print('Analizando o número {}'.format(num1))
u = num1 // 1 % 10
d = num1 // 10 % 10
c = num1 // 100 % 10
m = num1 // 1000 % 10
print('Milhar: {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(d))
print('Unidade: {}'.format(u))


/* Ver resolução */


# FUP que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

frase2 = str(input('Digite o nome da sua Cidade: '))
pedaco = frase2.upper().split()[0]
print('SANTO' in pedaco)

# FUP que leia o nome da pessoa e diga se ela tem "SILVA" no nome

frase3 = str(input('Digite seu nome: ')).upper()
print("SILVA" in frase3)

# FUP que leia uma frase pelo teclado e mostre:
    # Quantas vezes aparece a letra "A"
    # Em que posição ela aparece a primeira vez
    # Em que posição ela aparece a ultima vez

frase4 = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes'.format(frase4.count('A')))
print('Ela aparece na primeira vez na posição {}'.format(frase4.find("A")+1))
print('E aparece na ultima vez na posição {}'.format(frase4.rfind("A")+1))

# FUP que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
    # Ex: Ana Maria de Souza
    # primeiro: Ana
    # ultimo: Souza

frase5 = str(input('Digite o nome completo da pessoa: ')).upper().strip()
a = frase5.split()
print('Primeiro nome: {}'.format(a[0]))
print('Ultimo nome: {}'.format(a[len(a)-1]))
