## Questão 17 - Escreva um programa que use uma pilha para converter um número octal para decimal.

from pilha import Pilha

def octalparadecimal(vlr):
    p = Pilha()
    
    p.inserir(int(vlr, 8))
    
    return p._topo()

valor = input('Valor octal: ')
valorDecimal = octalparadecimal(valor)
print(valorDecimal)
