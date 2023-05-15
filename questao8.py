## Questão 8 - Escreva um programa que use uma pilha para 
# converter um número decimal para hexadecimal.

from pilha import Pilha

def decimalparahexadecimal(qct):
    p = Pilha()
    
    while qct > 0:
        resto = qct % 16
        match resto:
            case 10:
                p.inserir('A')
            case 11:
                p.inserir('B')
            case 12:
                p.inserir('C')
            case 13:
                p.inserir('D')
            case 14:
                p.inserir('E')
            case 15:
                p.inserir('F')
                
        qct = qct // 16
        
        if resto < 0:
            p.inserir(resto)
    
    return p

valor = int(input('Valor: '))
valorHexadecimal = decimalparahexadecimal(valor)

while not valorHexadecimal.is_empty():
    print(valorHexadecimal.remover(), end=' ')
    