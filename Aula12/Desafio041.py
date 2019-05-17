# A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
# sua categoria, de acordo com a idade:
# - Até 9 anos: Mirim
# - Até 14 anos: Infantil
# - Até 19 anos: Junior
# - Até 20 anos: Senior
# - Acima: Master

from datetime import datetime
ano = int(input('Informe a data de nascimento do Nadador: '))
idade = datetime.now().year - ano
if idade <= 9:
    print('Categoria MIRIM')
elif 9 < idade <= 14:
    print('Categoria INFANTIL')
elif 14 < idade <= 19:
    print('Categoria JUNIOR')
elif 19 < idade <= 20:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')
print('--FIM--')


print("""DADOS PARA INFORMAÇÃO:
        Ano de nascimento: {}
        Idade do Nadador: {}
        Ano atual: {}""".format(ano, idade, datetime.now().year))
