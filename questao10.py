## Questão 10 - Escreva um programa que use uma pilha para verificar 
# se uma expressão aritmética é válida. 
# A expressão é válida se para cada parêntese aberto houver 
# um parêntese fechado correspondente e, 
# para cada operação matemática, houver dois operandos.

from pilha import Pilha

def infixaparaposfixa(exp):
    preced = {'+': 1, '-': 1, '/': 2, '^': 3}
    operador = Pilha()
    posfixa = []
    num = '0123456789'
    for caracter in exp:
        if caracter in num:
            posfixa.append(caracter)
        elif caracter == '(':
            operador.inserir(caracter)
        elif caracter == ')':
            while operador._topo() != '(':
                posfixa.append(operador.remover())
            operador.remover()
        elif caracter in preced:
            while not operador.is_empty() \
                and operador._topo() != '(' \
                and preced[caracter] < preced[operador._topo()]:
                posfixa.append(operador.remover())
            operador.inserir(caracter)
    while not operador.is_empty():
        posfixa.append(operador.remover())
    return ''.join(posfixa)

def calcular(exp):
    p = Pilha()
    for caractere in exp:
        if caractere.isdigit():
            p.inserir(caractere)
        else:
            num2 = p.remover()
            num1 = p.remover()
            if caractere == '+':
                resultado = int(num1) + int(num2)
                p.inserir(str(resultado))
            elif caractere == '-':
                resultado = int(num1) - int(num2)
                p.inserir(str(resultado))
            elif caractere == '*':
                resultado = int(num1) * int(num2)
                p.inserir(str(resultado))
            elif caractere == '/':
                resultado = int(num1) / int(num2)
                p.inserir(str(resultado))
    return p.remover()

s = input('Expressão: ')
pos = infixaparaposfixa(s)
r = calcular(pos)
print(f'Expressão: {r}')

