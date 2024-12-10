int main(int argc, char *argv[]){

    //j'ouvre le fichier
    // je lis un caractere et je met dans buffer
    // et je ressors le texte dans un autre fichier ou sortie standard
    char str = getenv["MCAT_BUFSIZE"];
    if (str == NULL){
        fprint("str error");
    }
    int bufsize = atoi(str);
    if(bufsize <= 0){
        perror("MCAT_BUFSIZE n'est pas un entier positif");
        return -4;
    }
    int fd = open(argv[1,O_RDONLY]);
    if (fd < 0){
        perror("error open");
        return -3;
    }
    char *buffer = (char *)malloc(bufsize);
    if (buffer == NULL){
        perror("l'allocation de la mémoire a échoué");
        return EXIT_FAILURE;
    }

    int count;
    while(count=read(fd,buffer,bufsize) !=0){
        write(1,buffer,count);
    }

    free(buffer);
    close(fd);
    return 0;
}


#define MCAT_BUFSIZE 1024
int main(int argc, char* argv[]){
    int fd = open(argv[1,O_RDONLY]);
    if (fd < 0){
        perror("error open");
        return -3;
    }

    char t[MCAT_BUFSIZE];
    int count;
    while(count=read(fd,t,MCAT_BUFSIZE) !=0){
        write(1,t,count);
    }
    close(fd);
    return 0;

}

#define MCAT_BUFSIZE 1024
int main(int argc,char* argv[]){
    FILE * inputFile = fopen(argv[0], "r");
    if (inputFile = NULL){
        perror("fichier n'existe pas");
        return -4;
    }
    while(count=fgetc(inputFile) !=EOF){
        write(count,stdout);
    }
    fclose(inputFile);
    return 0;
}
