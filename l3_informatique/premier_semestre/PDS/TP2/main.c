#include <stdio.h>
#include <fcntl.h>
#include <dirent.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <string.h>

int du_file(const char *pathname);
int flagLienSymbo;


int main(int argc, char* argv[]){
    // int size=du_file("/home/l3miage/trevor.bruniaux.etu/Downloads");
    flagLienSymbo=0;
    if(argc==2){
        int size=du_file(argv[1]);
        printf("%d\n",size);
    }else if(argc==3){
        if(strcmp(argv[2],"-L")==0){
            flagLienSymbo=1;
            int size=du_file(argv[1]);
            printf("%d\n",size);
        }else{
            printf("Le deuxième argument doit être -L\n");
        }        
    }else if(argc==1){
        int size=du_file(".");
        printf("%d\n",size);
    }else{
        printf("Only 1 argument : Enter a pathname\n");
    }
    
}

int du_file(const char *pathname){
    DIR *d;
    struct dirent *ent;    
    int size=0;
    struct stat buf;

    d=opendir(pathname);
    if(d==NULL) {
        fprintf(stderr,"Warning : unable to open %s\n",pathname);
        exit(EXIT_FAILURE);
    }

    while((ent=readdir(d)) != NULL) {
        if(strcmp(".",ent->d_name)==0){
            stat(".",&buf);
            printf("%s : %ld\n", ent->d_name , buf.st_size);
            size+= buf.st_size;
        }
        
        if(strcmp(".",ent->d_name)!=0 && strcmp("..",ent->d_name)!=0){  
            char *name=malloc(PATH_MAX+1);
            sprintf(name,"%s/%s",pathname,ent->d_name);   
            if(flagLienSymbo==0){
                lstat(name,&buf);
            }else{
                stat(name,&buf);
            }
            DIR *directory;
            if ((directory = opendir(ent->d_name)) != NULL){
                closedir(directory);
                printf("\nDirectory : %s\n\n",ent->d_name);
                size+=du_file(name);
            }else{
                printf("%s : %ld\n", ent->d_name , buf.st_size);
                size+= buf.st_size;   
            }
        }
        
    }

    closedir(d);
    return size;
}
