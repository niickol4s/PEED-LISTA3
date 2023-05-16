## Questão 5 - Escreva um programa que use uma pilha para verificar 
# se uma string é um palíndromo (ou seja, se é igual quando lida de trás para frente).

from pilha import Pilha

def verificarpolindromo(plv):
    p = Pilha()
    
    palavraInvertida = ''
    
    for i in plv:
        p.inserir(i)
    
    while not p.is_empty():
        palavraInvertida += p.remover()
        
    return palavraInvertida == plv

string = input('Palavra: ')
strPolindromo = verificarpolindromo(string)
print(strPolindromo)  
    