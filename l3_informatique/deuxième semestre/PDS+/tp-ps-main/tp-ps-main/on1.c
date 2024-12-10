#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>

int execProg(char* argv[], int fst);

int main(int argc, char* argv[]){
    int i = 0;
    while (strcmp( argc[i], "do" ) !== 0 && i< argc){
        i++;
    }
    argv[i] = '\0';
    if (execProg(argv,1)==0){
        execProg(argv,i+1);
    }
    return EXIT_SUCCESS;
}

int execProg(char* argv[], int fst){
    pid_t pid ;
    pid = fork();
    if ( pid < 0) {
        execvp(argv[fst],&argv[fst]);
    }
    else{
        int stat=0;
        waitpid (pid, &stat,0);
        return WEXITSTATUS(stat);
    }
    return 0;
}
