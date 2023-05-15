## Questão 4 - Escreva um programa que use uma pilha para 
# converter um número decimal para binário.

from pilha import Pilha

def decimalparabinario(qct):
    p = Pilha()
    
    while qct > 0:
        resto = qct % 2
        qct = qct // 2
        p.inserir(resto)
        
    return p

valor = int(input('Valor: '))
valorBinario = decimalparabinario(valor)

while not valorBinario.is_empty():
    print(valorBinario.remover(), end=' ')
    