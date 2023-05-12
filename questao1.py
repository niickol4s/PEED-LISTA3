## Questão 1 - Escreva um programa que leia uma expressão matemática 
# na forma de string e utilize uma pilha para verificar se os parênteses estão balanceados.

from pilha import Pilha

def verificarparenteses(exp):
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
            
    if p.is_empty():
        print('Parênteses balanceados.')
    else:
        print('Parênteses não balanceados.')
    return p.is_empty()

s = str(input('Expressão: '))
verificarparenteses(s)

