import numpy as np 
from heap import *
from node import *

file = open("teste.txt", "r")
file2 = open("encoding.txt", "w")
text = file.read()
file.close()

dict_values = Node.get_frequency(text)

class Huffman:
    def __init__(self,lista):
        self.lista = lista
    def insere(self,lista):
        while len(lista) > 1:
            left = heapExtractMax(lista,len(lista))
            right = heapExtractMax(lista,len(lista))
            father= Node(left.freq+right.freq,None,left,right)
            maxHeapInsert(lista,father.freq,len(lista),father)
    def printRoot(self,root):
        print(root.freq)
    def printNodes(self,node):
        #if node.left != None:
        if node.left == None or node.left == None:
            return
        else:
            print(node.left.freq, node.right.freq)
        self.printNodes(node.left)
        self.printNodes(node.right)
    def printHuffmanTree(self,lista):
        self.printRoot(lista[0])
        self.printNodes(lista[0])
    def encoding(self,node,table,symbol,code):
        if node.left == None and node.left == None: #leaf node
            table.append(code)
            symbol.append(node.char)
            return
        self.encoding(node.left,table,symbol,code + "0")
        self.encoding(node.right,table,symbol,code + "1")
    def decoding(self,node,text,symbol):
        root = node
        for i in range(len(text)):
            if text[i] == '0':
                if node.left:
                    node = node.left
            elif text[i] == '1':
                if node.right:
                    node = node.right
            if node.left == None and node.left == None: #leaf node
                symbol.append(node.char)
                node = root
        
        

lista = []
table = []
symbol = []
decodification = []
code = ""
h = Huffman(lista)
freq = np.array(list(dict_values.values()))

for x, y in dict_values.items():
    h.lista.append(Node(y,x))
buildMaxHeap(lista,len(lista))
h.insere(lista)
h.encoding(lista[0],table,symbol, code)
for i in range(len(text)):
    file2.write(table[symbol.index(text[i])])
#print(table)
#print(symbol)
file2.close()
file3 = open("encoding.txt", "r")
file4 = open("decoding.txt", "w")
encod = file3.read()
#print(encod)
h.decoding(lista[0],encod,decodification)
file4.writelines(decodification)
#print(decodification)
