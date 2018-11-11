from heap import *
from node import *
from huffman import *
import argparse
def read_file(path):
    """
        Função que realiza a leitura do arquivo original de entrada. A função lê um determinado
        arquivo de entrada e cria um dicionário com as frequências de cada caracter.
        Parâmetros: path - caminho do arquivo original de entrada
        Return: text - uma lista numpy contendo os caracteres de leitura
                dict_values - um dicionário com os caracteres encontrados e suas respectivas frequências
    """
    file_original = open(path, "r")
    text = file_original.read()
    dict_values = Node.get_frequency(text)
    return text,dict_values
def encoding(h,huffman_tree,path):
    """
        Função que realiza o encoding baseado em um arquivo texto do usuário. Inicialmente, a função cria
        um nó folha com todos os caracteres encontrados e suas respectivas frequêncas, ordena utilizando uma lista de prioridade
        por min-heap e constrói a árvore de Huffman. Por fim, a função realiza o encoding dos caracters gravando o resultado
        em um arquivo.
        Parâmetros: h - objeto da classe Huffman utilizado para realizar o decoding
                    huffman_tree - lista com os nós da árvore de huffman
                    path - caminho do arquivo para decodificar
    """
    table = []
    symbol = []
    code = ""
    file_encoding = open("files/encoding.txt", "w")
    text,dict_values = read_file(path) #texto de entrada e dicionário com os caracteres e suas frequências
    for char, freq in dict_values.items(): #cria um nó folha com cada caracter encontrado no arquivo e suas respectivas sequências
        huffman_tree.append(Node(freq,char))
    buildMaxHeap(huffman_tree,len(huffman_tree)) #ordena a lista construindo um heap mínimo
    h.insere(huffman_tree) #constrói a árvore de huffman somando os nós de menor frequência do dicionário
    h.encoding(huffman_tree[0],table,symbol, code) #codifica a entrada
    for i in range(len(text)): #salva a codificação em um arquivo
        file_encoding.write(table[symbol.index(text[i])])

def decoding(h,huffman_tree,path):
    """
        Função que realiza o decoding baseado em um arquivo texto do usuário. Inicialmente, a função le um arquivo
        codificado, decodifica o mesmo utilizando a função decoding e escreve o resultado da mesma em um arquivo.
        Parâmetros: h - objeto da classe Huffman utilizado para realizar o decoding
                    huffman_tree - lista com os nós da árvore de huffman
                    path - caminho do arquivo para decodificar
    """
    decode = [] # lista com a decodificação do arquivo
    file_decoding = open("files/decoding.txt", "w")
    file_to_decode = open(path,"r")
    text = file_to_decode.read()
    h.decoding(huffman_tree[0],text,decode)
    file_decoding.writelines(decode)

def main():
    parser = argparse.ArgumentParser(description='Programa para realizar a codificação e decodificação de Huffman')
    parser.add_argument('-encode_path','--encode_path', help='Caminho do arquivo para codificar', required=True)
    parser.add_argument('-decode_path','--decode_path', help='Caminho do arquivo para decodificar', required=True)
    args = vars(parser.parse_args())
    huffman_tree = []
    h = Huffman(huffman_tree)
    encoding(h,huffman_tree,args['encode_path'])
    decoding(h,huffman_tree,args['decode_path'])
    
main()