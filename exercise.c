#include<stdio.h>

int main(void){
    /*char e;
    
    int c;
    for (c=0;c<3;c++){
        e =getchar();
        while(e!='\n'){
            printf("%c ",e);
            e=getchar();
        }
        printf("\n");
        if (e=='\n')
            e=' ';
    }*/
    int a [10];
    int *b;
    int c;
    b=a;
    for (c=0;c<10;c++){
        *b=10;
        b++;
    }
    for (c=0;c<10;c++)
        printf("%d ",a[c]);
    
    return 0;
}