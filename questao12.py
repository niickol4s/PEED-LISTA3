## Questão 12 - Escreva um programa que leia uma string contendo números 
# e use uma pilha para converter a string em um número decimal.

from pilha import Pilha

def strnumeroparadecimal(strnumero):
    p = Pilha()
    
    for i in strnumero:
        if i.isnumeric():
            int(i)
            p.inserir(i)
        else:
            IndexError('Valor inválido.')
    return p

strnumero = input('Valor: ')
numeroDecimal = strnumeroparadecimal(strnumero)

while not numeroDecimal.is_empty():
    print(numeroDecimal.remover(), end=' ')