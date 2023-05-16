## Questão 16 - Escreva um programa que use uma pilha para converter um número hexadecimal para decimal.

from pilha import Pilha

def hexadecimalparadecimal(vlr):
    p = Pilha()
    
    p.inserir(int(vlr, 16))
    
    return p._topo()

valor = input('Valor hexadecimal: ')
valorDecimal = hexadecimalparadecimal(valor)
print(valorDecimal)
