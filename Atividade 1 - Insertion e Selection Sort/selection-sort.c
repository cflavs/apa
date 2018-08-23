#include <stdio.h>
#include <stdlib.h>

int main() {

    FILE *f;
    char c;
    f=fopen("couting.txt","r");
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
