#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>



int main(int argc, char **argv){
    if(argc==2){
        char* pathname=argv[1];
        FILE* file=fopen(pathname,"r");
        if(file!=NULL){
            int currentChar;
            while((currentChar=(fgetc(file)))!=EOF){                
                fputc(currentChar,stdout);
            }
            return 0;
        }
    }
    return -1;
}