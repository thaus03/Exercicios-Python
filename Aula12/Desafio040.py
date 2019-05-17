#  Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# - Média abaixo de 5.0: Reprovado
# - Média entre 5.0 e 6.9: Recuperação
# - Média acima de 7.0: Aprovado

cores = {'limpa': '\033[m',
         'vermelhoi': '\033[7;31m',
         'verdei': '\033[7;32m',
         'amareloi': '\033[7;33m',
         'cianos': '\033[4;36m',
         'cinzas': '\033[4;37m'
         }
nota1 = float(input('{}Informe a nota da primeira Avaliação:{} '.format(cores['cianos'], cores['limpa'])))
nota2 = float(input('{}Informe a nota da segunda Avaliação:{} '.format(cores['cinzas'], cores['limpa'])))
media = (nota1 + nota2)/2
if media < 5.0:
    print('{}REPROVADO{}'.format(cores['vermelhoi'], cores['limpa']))
elif 5.0 < media < 6.9:
    print('{}RECUPERAÇÃO{}'.format(cores['amareloi'], cores['limpa']))
else:
    print('{}APROVADO{}'.format(cores['verdei'], cores['limpa']))
print('--FIM--')