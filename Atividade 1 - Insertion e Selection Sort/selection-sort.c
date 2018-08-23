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
    int n = 100;
    int i_min,temp;

    for (int i = 0; i < n; i++){
        fscanf(f, "%d", &instancias[i]);
    }
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
    for(int i=0;i<n;i++)
        printf("%d\n", instancias[i]);
    fclose(f);
    return 0;
}
