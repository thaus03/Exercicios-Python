# print('\033[7;33;44mOlá mundo!\033[m')

# Adicionando no print
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))


# Utilizando no format
nome = 'Igor'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;36m', nome, '\033[m'))


# Utilizando dicionário
nome = 'Igor'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))