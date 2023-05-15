## Questão 11 - Escreva um programa que use uma pilha para 
# ordenar uma lista de números em ordem crescente.

from pilha import Pilha

def ordemcrescente(lista):
    p = Pilha()
    listaordenada = []
    
    for i in lista:
        listaordenada.append(i)
    
    listaordenada.sort(reverse=True)
    
    for i in listaordenada:
        p.inserir(i)
    
    return p

lista = list()

tam = int(input('Tamanho: '))

for i in range(tam):
    lista.append(int(input('Valor: ')))

valoresordenados = ordemcrescente(lista)

while not valoresordenados.is_empty():
    print(valoresordenados.remover())

    