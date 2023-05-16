## Questão 7 - Escreva um programa que use uma pilha para converter um número decimal para octal.

from pilha import Pilha

def decimalparaoctal(qct):
    p = Pilha()
    
    while qct > 0:
        resto = qct % 8
        qct = qct // 8
        p.inserir(resto)
    
    return p

valor = int(input('Valor: '))
valorOctal = decimalparaoctal(valor)

while not valorOctal.is_empty():
    print(valorOctal.remover(), end='')
