frase = "Curso em Vídeo Python"
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[::2])

print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.""")

print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
print(frase.find('deo'))
print(frase.split())
print(frase.split()[2][3])

# -======================================================
frase2 = "     Curso em Vídeo Python    "
print(len(frase2))
print(len(frase.strip()))
