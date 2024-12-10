#include "answers.h"

#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <semaphore.h>
#include <string.h>
#include <limits.h>






void liste_sous_reps(*pathname){
    DIR *d;
}




















/*EXO1 */
void liste_sous_reps(char *dirname){
    DIR *d;
    struct dirent *ent;
    struct stat buf;
    d = opendir(dirname);
    while(ent = readdir(d)!NULL){
        char *name = malloc (1024);
        sprintf(name,"%s%s", dirname, ent->d.name);
        stat(name, &buf);
        if(strcmp(".", ent->d.name) != 0 && (strcmp(".."), ent->d.name) !=0){
            affiche_str(name);
        }
        
    }
}





struct sem{
    sem_t attente;
    sem_t bloquage;
}
struct sem ex;
void init(int nb_threads){
    for (int i = 0; i<nb_threads; i++){{
    }
        sem_init((&ex.bloquage),0,0);
    }
}

void activate(int nb_threads){
    for (int i = 0; i<nb_threads; i++){
        sem_wait(&ex.attente);
    }
    for (int i = 0; i<nb_threads; i++){
        sem_post(&ex.bloquage);
    }
}

void synchro(int i){
    for (int i = 0; i<nb_threads; i++){
        sem_post(&ex.bloquage);
        sem_wait(&ex.attente);
    } 
}



