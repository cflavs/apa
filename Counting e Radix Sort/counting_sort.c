#include <stdio.h>
#include <stdlib.h>

void counting_sort(int A[],int B[],int n, int exp, int k){
    int C[k];
    for(int i=0;i<k;i++)
        C[i] = 0; //inicializa vetor
    
    for (int j=0; j<n;j++){
        C[A[j]] += 1; //calcula a frequencia dos valores
    }
    for (int i=0;i<k-1;i++){
        C[i+1] = C[i] + C[i+1];
    }

    int aux=0;
    for(int i=n-1;i>-1;i--){ //ordena 
        aux = A[i];
        C[aux]-=1;
        B[C[aux]]=aux;
    }
}
int main(int argc, char* argv[]) {
    FILE *f;
    char *filename;
    //int A[8] = {2, 5, 3, 0, 2, 3, 0, 3};
    int A[100];
    int B[100];
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
    // encontrar maximo valor
    int k=A[0];
    for(int i=1;i<n;i++){
        if(A[i] > k)
            k = A[i];
    }
    k+=1;

    /////Counting-sort
    //counting_sort(A,B,n);

    /// Radix-sort
    for (int exp = 1; k/exp > 0; exp *= 10)
        counting_sort(A, B, n, exp,k);
    //Exibe instancias ordenadas
    for(int i=0;i<n;i++)
        printf("%d\n", B[i]);

    fclose(f);
    return 0;
}
