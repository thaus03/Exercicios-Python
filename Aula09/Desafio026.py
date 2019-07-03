# Faça um programa que leia uma frase pelo teclado e mostre:
#     # Quantas vezes aparece a letra "A"
#     # Em que posição ela aparece a primeira vez
#     # Em que posição ela aparece a ultima vez

frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra "A" aparece {frase.count("A")} na frase digita')
print(f'Ele aparece a primeira vez na posição {frase.find("A") +1}.')
print(f'Ele aparece a ultima vez na posição {frase.rfind("A") +1}')
print('--FIM--')
