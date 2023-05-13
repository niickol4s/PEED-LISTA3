## Questão 6 - Escreva um programa que leia uma string contendo caracteres (, ), 
# {, }, [ e ], e use uma pilha para verificar se os caracteres estão balanceados.

from pilha import Pilha

def caracteresbalanceados(exp):
    p = Pilha()
    num = '0123456789'
    expressao = []
    for i in exp:
        if i in num:
            expressao.append(i)
        elif i == '(':
            p.inserir(i)
        elif i == ')':
            p.remover()
        elif i == '{':
            p.inserir(i)
        elif i == '}':
            p.remover()
        elif i == '[':
            p.inserir(i)
        elif i == ']':
            p.remover()
    if p.is_empty():
        print('Caracteres balanceados.')
    else:
        print('Caracteres não balanceados.')
    return p.is_empty()

s = input('Expressão: ')
caracteresbalanceados(s)
