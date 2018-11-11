import numpy as np 
from heap import *
from node import *

class Huffman:
    def __init__(self,lista):
        self.lista = lista
    def insere(self,lista):
        """
            Função que constrói a árvore de Huffman propriamente dita. Enquanto a lista possui mais que um elemento, 
            a função encontra os dois elementos de menor frequência da lista e cria um nó pai que possui como frequência
            a soma das duas menores frequências calculadas posteriormente. 
            Parâmetros: lista - lista com os nós da árvore de huffman
        """
        while len(lista) > 1: #enquanto a lista possui mais que um elemento (i.e. enquanto a lista não possui apenas um nó com a raiz da árvore)
            left = heapExtractMin(lista,len(lista)) #encontra o menor nó da lista
            right = heapExtractMin(lista,len(lista)) #encontra o segundo menor nó da lista
            father= Node(left.freq+right.freq,None,left,right) #cria um nó pai tendo como filhos os dois menores nós da lista
            heapInsert(lista,father.freq,len(lista),father) #insere o nó pai na árvore utilizando de forma a manter a propriedade de min-heap
    def printRoot(self,root):
        """
            Função que exibe o nó raiz da árvore
            Parâmetro: root - o nó raiz
        """
        print(root.freq)
    def printNodes(self,node):
        """
            Função que exibe os nós filhos da árvore de acordo com o nível da árvore.
            Parâmetros: o nó pai atual
        """
        if node.left == None or node.left == None:
            return
        else:
            print(node.left.freq, node.right.freq)
        self.printNodes(node.left)
        self.printNodes(node.right)
    def printHuffmanTree(self,lista):
        """
            Função que exibe a árvore completa de acordo com a profundidade da mesma. Inicilamente, a função
            exibe o nó real da árvore e, posteriormente, exibe os nós filhos de cada nível recursivamente.
        """
        self.printRoot(lista[0])
        self.printNodes(lista[0])
    def encoding(self,node,table,symbol,code):
        """
            Função que raliza a codificação de huffman. Na função, enquanto um nó folha não é encontrado, a função é 
            chamada recursivamente pelos filhos da esquerda e da direita.
            Parâmetros: node - nó pai atual da árvore
                        table - uma lista com os códigos de cada símbolo
                        symbol - o caracter folha encontrado na árvore correspondente ao código
                        code - código binário da árvore

        """
        if node.left == None and node.left == None: #leaf node
            table.append(code)
            symbol.append(node.char)
            return
        self.encoding(node.left,table,symbol,code + "0")
        self.encoding(node.right,table,symbol,code + "1")
    def decoding(self,node,text,symbol):
        """
            Função que realiza a decodificação de huffman. Na função, a árvore de huffman é percorrida levando-se em
            consideração os caracteres do texto. Onde se o caracter é igual a 0, a árvore percorre o filho da esquerda 
            caso contrário, percorre, o filho da direita, até que um nó folha seja encontrado. Ao encontrar um nó folha,
            o algoritmo retorna para o nó raiz.
        """
        root = node #nó raiz
        for i in range(len(text)):
            if text[i] == '0':
                if node.left:
                    node = node.left #se o caracter decodificado possui valor 0, percorre o filho da esquerda
            elif text[i] == '1':
                if node.right:
                    node = node.right #se o caracter decodificado possui valor 1, percorre o filho da direita
            if node.left == None and node.left == None: 
                symbol.append(node.char) #se a árvore não possui mais filhos, armazena o valor do caracter encontrado e retorna para o nó raiz
                node = root
        