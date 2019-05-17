nome = str(input('Qual é o seu nome? '))
if nome == 'Igor':
    print('\033[0;34mQue nome bonito!\033[m')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in ('Ana Claudia Jéssica Juliana'):
    print('\033[7;30mBelo nome feminino\033[m')
else:
    print('Seu nome é muito normal')
print('Tenha um bom dia, {}!'.format(nome))
