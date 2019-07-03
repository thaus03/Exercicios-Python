# Desafio 083
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechado e na ordem correta.


# exprecao = []
# frase = str(input('Digire aqui sua expressão: '))
# for i in frase:
#     exprecao.append(i)
# if exprecao.count("(") == exprecao.count(")"):
#     print('Expressão válida')
# elif exprecao.count("(") > exprecao.count(")"):
#     print('Expressão inválida! Faltando parêntese direito.')
# elif exprecao.count("(") < exprecao.count(")"):
#     print('Expressão inválida! Faltando parêntese esquerdo.')
# print(f'A expressão digitada foi {exprecao}')


##### SOLUÇÃO DO PROFESSOR ######

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada')

