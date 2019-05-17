# Escreva um programa para aprovar o empréstimo bancario para a compra de uma casa. O programa
# vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
# o emprestimo será negado.

val = float(input('\033[4;31mQual é o valor do imóvel?\033[m '))
sal = float(input('\033[4;32mInforme seu salário:\033[m '))
ano = int(input('\033[7;33mEm quantos anos vocẽ pretende parcelar?\033[m '))
parcela = (sal*30)/100
prest_mensal = val / (ano * 12)
if parcela < prest_mensal:
    print('Emprestimo negado')
else:
    print('Emprestimo aprovado')

print("""Valores informativos:
    Valor da prestação: R$ {:.2f}
    Valor da Parcela: R$ {:.2f}""".format(prest_mensal, parcela))
print('--FIM--')
