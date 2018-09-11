#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    FILE *f;
    char *filename;
    int instancias[5000];
    int n = 100, pivo=0,j=0;
    
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
        fscanf(f, "%d", &instancias[i]);
    }
    //Insertion-sort
    for(int i=0;i<n;i++){
        pivo = instancias[i];
        j = i-1;
        while(j>=0 && instancias[j]>pivo){
            instancias[j+1] = instancias[j];
            j=j-1;
        }
        instancias[j+1] = pivo;
    }
    //Exibe instancias ordenadas
    for(int i=0;i<n;i++)
        printf("%d\n", instancias[i]);
    fclose(f);
    return 0;
}
