# Faça um programa qe leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# - Se ele ainda vai se alistar ao serviço militar | Se é a hora de se alistar. | - Se já passou do tempo de alistamento
# Seu programa também deverá mostrar o tempo que falta ou passou do prazo.
from datetime import datetime
from math import fabs
ano = int(input('\033[1;35mInforme o ano de seu nascimento (YYYY):\033[m '))
diff = datetime.now().year - ano
if diff < 18:
    print("""Você ainda precisa se alistar ao serviço militar!
        Faltam {:.0f} anos para você""".format(18 - diff))

elif diff == 18:
    print('Chegou a hora de você se alistar ao serviço militar')
else:
    print("""Você já passou do tempo de alistamento
        Você já passou {:.0f} anos""".format(fabs(18 - diff)))
print('--FIM--')
