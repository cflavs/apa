#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    FILE *f;
    char *filename;
    if(argc != 2)
    {
        printf( "Missing filename");
        return 0; //should be two arguments, exe name & file path/name
    }
    else{
        filename=argv[1];
    }
    f=fopen(filename,"r");

    int instancias[5000];
    int n = 100, pivo=0,j=0;

    for (int i = 0; i < n; i++){
        fscanf(f, "%d", &instancias[i]);
    }
    for(int i=0;i<n;i++){
        pivo = instancias[i];
        j = i-1;
        while(j>=0 && instancias[j]>pivo){
            instancias[j+1] = instancias[j];
            j=j-1;
        }
        instancias[j+1] = pivo;
    }
    for(int i=0;i<n;i++)
        printf("%d\n", instancias[i]);
    fclose(f);
    return 0;
}
