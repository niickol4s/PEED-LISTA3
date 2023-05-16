## Questão 20 - Escreva um programa que use uma pilha para 
# converter um número binário para hexadecimal.

from pilha import Pilha

def binarioparahexadecimal(qct):
    p = Pilha()
    dcm = 0
    
    for i in range(len(qct)):
        dcm += int(qct[i]) * pow(2, len(qct) - i -1)
        
        while dcm > 0:
                
            resto = dcm % 16
                
            match resto:
                case 1010:
                    p.inserir('A')
                case 1011:
                    p.inserir('B')
                case 1100:
                    p.inserir('C')
                case 1101:
                    p.inserir('D')
                case 1110:
                    p.inserir('E')
                case 1111:
                    p.inserir('F')
                case _:
                    p.inserir(resto)
                
            dcm = dcm // 16
        
    return p._topo()

valor = input('Valor: ')
valorHexadecimal = binarioparahexadecimal(valor)
print(valorHexadecimal)
    