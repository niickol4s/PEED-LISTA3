## Questão 13 - Escreva um programa que use uma pilha 
# para converter um número binário para decimal.

from pilha import Pilha
from math import pow

def binarioparadecimal(num):
    p = Pilha()
    dec = 0
    
    for i in range(len(num)):
        dec += int(num[i]) * pow(2, len(num) - i - 1)
    
    while dec > 0:
        p.inserir(dec % 10)
        dec = dec // 10
    
    return p

valor = input('Valor binário: ')
valorDecimal = binarioparadecimal(valor)

while not valorDecimal.is_empty():
    print(valorDecimal.remover(), end=' ')
    