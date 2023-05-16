## Questão 12 - Escreva um programa que leia uma string contendo números 
# e use uma pilha para converter a string em um número decimal.

from pilha import Pilha

def strnumeroparadecimal(strnumero):
    p = Pilha()
    
    for i in range(len(strnumero) -1, -1, -1):
        
        if strnumero[i].isnumeric():
            p.inserir(int(strnumero[i]))
        
    return p

strnumero = input('Valor: ')
numeroDecimal = strnumeroparadecimal(strnumero)

while not numeroDecimal.is_empty():
    print(numeroDecimal.remover(), end='')
    
    