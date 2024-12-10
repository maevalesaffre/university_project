#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char **argv){
    if(argc==3){
        int bufferSize=atol(argv[1]);
        char* pathname=argv[2];
        char* buffer=malloc(sizeof(char)*bufferSize);
        int fd=open(pathname,O_RDONLY);
        if(fd!=-1){
            int readSize;
            while((readSize=read(fd,buffer,bufferSize))>0){
                write(1,buffer,readSize);
            }
            return 0;
        }
    }
    return -1;
}