#include  <stdio.h>
#include  <sys/types.h>
#include  <stdlib.h>
#include  <sys/stat.h>
#include <fcntl.h>
#include  <error.h>
#include  <wait.h>
#include  <unistd.h>
#include <string.h>


int main(void){
    int fd[2];
    int fd1[2];
    int num1,num2,num3;
    char word1 [ ] ="child process 1 is sending message";
    char word3 [ ] ="child process 2 is sending message";
    char word5 [ ] ="child process 3 is sending message";
    char word2 [35];
    char word4[35];
    char word6[35];
    pipe(fd);
    pipe(fd1);
    num1=fork();
    if (num1==0){
        write(fd[1],word1,35);
        exit(0);
    }
    else{
        //wait(0);
        read(fd[0],word2,35);
        printf("%s\n",word2);
  
    }
    num2 = fork();
    if (num2==0){
        write(fd[1],word3,35);
        exit(0);
    }
    else{
        //wait(0);
        read(fd[0],word4,35);
        printf("%s\n",word4);
    }
    num3 = fork();
    if (num3==0){
        write(fd[1],word5,35);
        exit(0);
    }
    else{
        //wait(0);
        read(fd[0],word6,35);
        printf("%s\n",word6);
    }

    
    
    return 0;

}