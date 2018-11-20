# Estrutura de Dados e Complexidade de Algoritmos

Esse repositório contém as implementações dos algoritmos vistos na disciplina de Estrutura de Dados e Complexidade de Algoritmos. 

## Estrutura do Repositório

Esse repositório é organizado de acordo com dois diretórios principais: Sorting Algorithms e Huffman

### Sorting Algorithms

Contém implementação dos algoritmos de inserção, seleção, counting, ratix e max-heap utilizando a linguagem de programação C. Cada algoritmo possui um diretório correspondente com os arquivos fontes, um makefile e um arquivo texto com instâncias de teste para ordenar. Para compilar, utilize o comando abaixo dentro do diretório do algoritmo a ser utilizado:

```sh
$ make
```
Posteriormente, para rodar o algoritmo, utilize o comando:
```sh
$ ./nome_do_executavel couting.txt
```
Em que, nome_do_executavel é o nome do arquivo criado após o comando make e couting.txt o nome do arquivo com as instâncias de teste.

### Huffman 

Contém a implementação do algoritmo de huffman para codificação e decodificação utilizando a linguagem de programação Python. Para rodar o algoritmo, utilize o comando abaixo dentro do diretório Huffman:
```sh
$ python3 main.py -encode_path files/nome_do_arquivo_teste.txt -decode_path files/encoding.txt
```
Em que, nome_do_arquivo_teste é o nome do arquivo com o texto a ser codificado e files/encoding.txt é o arquivo codificado gerado pelo próprio algoritmo Huffman após a codificação. Dois exemplos de arquivos textos podem ser encontrados no diretório Huffman/files (abracadabra.txt e lorem.txt).

### Metaheuristica

Contém a implementação do algoritmo de clusterização K-means, e da metaheuristica Variable neighborhood search (VNS) utilizando Python. Para rodar o algoritmo, utilize o comando abaixo dentro do diretório Huffman:

```sh
$ python3 heuristics.py
```


