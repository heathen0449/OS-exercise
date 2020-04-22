#include<stdio.h>
#include<stdlib.h>
void show(char *a, char *b, char *c);
void init(char *a, char *b, char *c);
void choose(char *a,char *b,char *c);
void operation_1(char *a,char *b);
int find(char *a_point);

int main(void){
    char ready_arr[15];
    char block_arr[15];
    char doing_arr[15];
    init(ready_arr,doing_arr,block_arr);
    show(ready_arr,doing_arr,block_arr);
    choose(ready_arr,doing_arr,block_arr);
    return 0;
}

int  find (char *a_point){
    int b_point;
    b_point=0;
    while(a_point[b_point]!=' '){
        b_point++;
    }
    return --b_point;
}

void show(char*a,char *b,char*c){
    int z,flag_a,flag_b,flag_c;
    if(a[0]==' ')
        printf("就绪队列为空\n");
        flag_a=1;
    if(b[0]==' ')
        printf("执行队列为空\n");
        flag_b=1;
    if(c[0]==' ')
        printf("阻塞队列为空\n");
        flag_c=1;
    printf("就绪队列内容为:");

    for (z=find(a);z>=0;z--){
        if (a[z]>='A' && a[z]<='O' )
            printf("%c ",a[z]);
    }
    printf("\n");
    printf("执行队列内容为:");
    for (z=find(b);z>=0;z--){
        if (b[z]>='A' && b[z]<='O' ) 
            printf("%c ",b[z]);
    }
    printf("\n");
    printf("阻塞队列内容为：");
    for (z=find(c);z>=0;z--){
        if (c[z]>='A' && c[z]<='O' )
            printf("%c ",c[z]);
    }
    printf("\n");
}

void init(char *a, char *b, char *c){
    int num; //用于初始化状态数组
    int number_a,number_b,number_c=0;//用于初始化三个进程对列
    int state[15];
    int number1;
    char story;
    int count;
    for (num =0;num<15;num++){
        a[num]=b[num]=c[num]=' ';
    }
    printf("请输入预设队列\n");
    printf("顺序为就绪、执行、阻塞,从队尾到队首\n");
    for(number1=0;number1<15;number1++){
        state[number1]=0;
    }
    number1 =0;
    for (number1=0;number1<3;number1++){
        story=getchar();
        while(story!='\n'){
            //count=0;
            if (story<= 'Z'&& story>= 'A' && state[story-'A']==0 ){
                //count++;
                //if(count>14)
                    //printf("数量越界，重新输入\n");
                    //break;
                state[story-'A']=1;
                switch (number1){
                    case 0:
                        a[number_a]=story;
                        number_a++;
                        break;
                    case 1:
                        b[number_b]=story;
                        number_b++;
                        break;
                    case 2:
                        c[number_c]=story;
                        number_c++;
                }
                story=getchar();
            }
            else
            {
                printf("输入非法，请重新输入\n");
                story=getchar();
                continue;
            }   
        }
        if (story=='\n')
            story=' ';
    }    
}

void operation_1 (char*a,char*b){
    int n1,n2;
    n1=find(a);
    n2=find(b);
    int c;
    for (c=n2;c>=0;c--){
        b[c+1]=b[c];
    }
    b[0]=a[n1];
    a[n1]=' ';
}

void choose(char *a, char*b,char*c){
    int order;
    int detect;
    int detect1;
    int index;
    int noun;
    int flag; //4号的标志
    printf("请输入您的命令(整数2-4),输入0则退出：\n");
    scanf("%d",&order);
    if (order==0) return;
    while(order<=1||order>=5){
        printf("输入命令无法识别，请重新输入\n");
        printf("请输入您的命令(整数2-4)：\n");
        scanf("%d",&order);
    }
    while(order!=0){
        if(order>1&&order<5){
            switch(order){
                case 2:
                    detect=find(b);
                    if (detect>=0){
                        detect1=find(a);
                        if (detect1>=0){
                            for(noun=detect1;noun>=0;noun--){
                                a[noun+1]=a[noun];
                            }
                        }
                        a[0]=b[detect];
                        b[detect]=' ';
                        operation_1(a,b);
                        show(a,b,c);
                        break;
                    }
                    else
                    {
                        printf("无法执行进行态转换就绪态，请重新输入命令\n");
                        break;
                    }
                case 3:
                    detect = find(b);
                    if(detect>=0){
                        detect1=find(c);
                        if(detect1>=0){
                            for (noun=detect1;noun>=0;noun--){
                                c[noun+1]=c[noun];
                            }
                        }
                        c[0]=b[detect];
                        b[detect]=' ';
                        index=find(a);
                        if(index>=0){
                            operation_1(a,b);
                        }
                        show(a,b,c);
                        break;
                    }
                    else{
                        printf("无法执行此操作\n");
                        break;
                    }
                case 4:
                    detect= find(c);
                    if (detect>=0){
                        detect1=find(a);
                        if(detect1>=0)
                        for (noun=detect1;noun>=0;noun--){
                            a[noun+1]=a[noun];
                        }
                        index=find(b);
                        a[0]=c[detect];
                        c[detect]=' ';
                        if(detect1==-1 &&index==-1){
                            operation_1(a,b);
                        }
                        show(a,b,c);
                        break;
                    }
                    else{
                        printf("无法执行此命令，请重新输入\n");
                    }
            }
            printf("请输入您的命令(整数2-4),输入0则退出：\n");
            scanf("%d",&order);
        }
    }
    
}