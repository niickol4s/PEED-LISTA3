## Questão 15 - Escreva um programa que leia uma string contendo números 
# e use uma pilha para converter a string em um número binário.

from pilha import Pilha

def stringdecimalparabinario(vlr):
    p = Pilha()
    
    while vlr > 0:
        resto = vlr % 2
        vlr //= 2
        p.inserir(resto)
        
    return p

numero = int(input('Número: '))
resultado = stringdecimalparabinario(numero)

while not resultado.is_empty():
    print(resultado.remover(), end='')
