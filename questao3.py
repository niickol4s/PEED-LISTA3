## Questão 3 - Escreva um programa que leia uma string contendo 
# números e operações matemáticas (+, -, *, /) e use uma pilha para 
# calcular o resultado da expressão.

from pilha import Pilha

def infixaparaposfixa(exp):
    preced = {'+': 1, '-': 1, '/': 2, '^': 3}
    operador = Pilha()
    posfixa = []
    num = '0123456789'
    for caracter in exp:
        if caracter in num:
            posfixa.append(caracter) ##
        elif caracter in preced:
            while not operador.is_empty() \
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
                