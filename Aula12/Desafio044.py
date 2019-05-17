# FUP que elabore o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento.
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: Preço normal
# - 3x ou mais no cartão: 20% de juros

preco = float(input('Informe o preço do produto (APENAS NUMEROS): '))
cond = int(input("""Informe opção referente a confição de pagamento:
1 - À vista em dinheiro ou cheque
2 - À vista no cartão
3 - Em até 2x no cartão
4 - 3x ou mais no cartão
Opção: """))
if cond == 1:
    desc = (preco * 10)/100
    print('O novo valor do produto será de R$ {:.2f}'.format(preco - desc))
elif cond == 2:
    desc = (preco * 5) / 100
    print('O novo valor do produto será de R$ {:.2f}'.format(preco - desc))
elif cond == 3:
    print('O valor do produto mantem em R$ {:.2f}'.format(preco))
elif cond == 4:
    juros = (preco * 20) / 100
    print('O novo valor do produto será de R$ {:.2f}'.format(preco + juros))
else:
    print('Opção Indisponível, tente novamente! ')
print('--FIM--')