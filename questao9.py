## Questão 9 - Escreva um programa que leia uma string contendo apenas números 
# e use uma pilha para verificar se a string é um número de palíndromo.

from pilha import Pilha

def verificarvalorpolindromo(vlr):
    p = Pilha()
    numeroInvertido = ''
    
    for i in vlr:
        p.inserir(i)
    
    while not p.is_empty():
        numeroInvertido += p.remover()
    
    return numeroInvertido == vlr

valor = input('Valor: ')
valorPolindromo = verificarvalorpolindromo(valor)
print(valorPolindromo)
    