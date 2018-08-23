#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    FILE *f;
    char *filename;
    int instancias[5000];
    int n = 100;
    int i_min,temp;

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
    //Selection-sort
    for (int i = 0; i < (n-1); i++) 
    {
        i_min = i; 
        for (int j = (i+1); j < n; j++) {
        if(instancias[j] < instancias[i_min]) 
            i_min = j;
        }
        if (instancias[i] != instancias[i_min]) {
            temp = instancias[i];
            instancias[i] = instancias[i_min];
            instancias[i_min] = temp;
        }
    }
    //Exibe instancias ordenadas
    for(int i=0;i<n;i++)
        printf("%d\n", instancias[i]);
    fclose(f);
    return 0;
}
