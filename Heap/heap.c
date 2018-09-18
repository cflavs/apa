#include <stdio.h>
#include <stdlib.h>

void trocar(int * a, int *b) {
	int  aux = *a;
	*a = *b;
	*b = aux;
}

void maxHeapify(int A[], int tamanho_heap, int i)
{
    int maior = i; 
    int esquerda = 2*i;
    int direita = 2*i + 1; 
 
    if (esquerda < tamanho_heap && A[esquerda] > A[maior])
        maior = esquerda;
    else
        maior = i;
    if (direita < tamanho_heap && A[direita] > A[maior])
        maior = direita;
 
    if (maior != i)
    {
        trocar(&A[i], &A[maior]);
        maxHeapify(A, tamanho_heap, maior);
    }
}

void buildMaxHeap(int A[],int tamanho_heap){
     for (int i = tamanho_heap/2 - 1; i >= 0; i--)
        maxHeapify(A, tamanho_heap, i);   
}
void heapSort(int A[], int tamanho_heap)
{
    buildMaxHeap(A,tamanho_heap);
    for (int i=tamanho_heap-1; i>=0; i--)
    {
        trocar(&A[0], &A[i]);
        maxHeapify(A, i, 0);
    }
}
 
int main(int argc, char* argv[])
{
    FILE *f;
    char *filename;
    int A[100];
    int n = 100;
    
    //Verifica se o usuário incluiu o nome do arquivo como parametro do programa
    if(argc != 2)
    {
        printf("Falta o nome do arquivo a ser ordenado como parametro do programa");
        return 0; 
    }
    else{
        filename=argv[1];
    }
    //Leitura do arquivo
    f=fopen(filename,"r");
    for (int i = 0; i < n; i++){
        fscanf(f, "%d", &A[i]);
    }

    heapSort(A, n);
    for (int i=0; i<n; i++)
        printf("%d\n", A[i]);
}