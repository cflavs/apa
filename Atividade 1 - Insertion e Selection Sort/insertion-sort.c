#include <stdio.h>
#include <stdlib.h>

int main() {

    FILE *f;
    char c;
    f=fopen("couting.txt","r");
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
