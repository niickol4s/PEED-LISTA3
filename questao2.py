## Questão 2 - Escreva um programa que leia uma string 
# e use uma pilha para inverter a ordem das palavras.

from pilha import Pilha

def inverterordem(lista):
    p = Pilha()
    
    for i in lista:
        p.inserir(i)
    return p

stingpalavra = input('Palavras: ').split()
palavrainvertida = inverterordem(stingpalavra)

while not palavrainvertida.is_empty():
    print(palavrainvertida.remover(), end=' ')

        