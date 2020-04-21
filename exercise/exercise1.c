#include<stdio.h>
 
void show(char *a, char *b, char *c);
void init(char *a, char *b, char *c);
void choose(int order);
 
int main(void){
    char ready_arr[15];
    char block_arr[15];
    char doing_arr[15];
    show(ready_arr,block_arr,doing_arr);

    return 0;
}

void show(char*a,char *b,char*c){
    int z,flag_a,flag_b,flag_c;
    if(a[0]==' ')
        printf("就绪队列为空\n");
        flag_a=1;
    if(b[0]==' ')
        printf("执行队列为\n");
        flag_b=1;
    if(c[0]==' ')
        printf("等待队列为空\n");
        flag_c=1;
    printf("就绪队列内容为:");
    for (z=0;z<15;z++){
        if (a[z]>='A' && a[z]<='Z' )
            printf("%c ",a[z]);
    }
    printf("\n");
    printf("运行队列内容为:");
    for (z=0;z<15;z++){
        if (b[z]>='A' && b[z]<='Z' ) 
            printf("%c ",b[z]);
    }
    printf("\n");
    printf("阻塞队列内容为");
    for (z=0;z<15;z++){
        if (c[z]>='A' && c[z]<='Z' )
            printf("%c ",c[z]);
    }
}

void init(char *a, char *b, char *c){
    int num;
    for (num =0;num<15;num++){
        a[num]=b[num]=c[num]=' ';
    }
    
}