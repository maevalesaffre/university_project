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


/* Exercice 1 */
void liste_sous_reps(char* dirname)
{
    DIR *d;
    struct dirent *ent;
    struct stat buf;

    d=opendir(dirname);

    while((ent=readdir(d)) != NULL){
        char *name=malloc(1024);
        sprintf(name,"%s%s",dirname,ent->d_name); 
        stat(name,&buf);
        if(strcmp(".",ent->d_name) !=0 && strcmp("..",ent->d_name) !=0 && S_ISDIR(buf.st_mode)){
            affiche_str(name);
        }
        
    }
}

/* Exercice 2 */
struct sem{
    sem_t *attente;
    sem_t controle;
    
};
struct sem ex;

void init(int nb_threads)
{
    ex.attente=malloc(sizeof(sem_t)*nb_threads);
    for(int i=0;i<nb_threads;i++){
        sem_init(&ex.attente[i],0,0);
    }
    sem_init(&ex.controle,0,(nb_threads)*-1);
    
}

void synch(int i)
{    
    // if(i+1==ex.taille){
    //     sem_post(&ex.controle);
    //     // Je libère le controle avant d'attendre le dernier. 
    //     // Il faudrait que j'arrive à le libérer après avoir fait attendre le dernier.
    // }
    // sem_wait(&ex.attente[i]);
    sem_post(&ex.controle);
    sem_wait(&ex.attente[i]);
    
}

void activate(int nb_threads)
{
    for(int i=0;i<nb_threads;i++){
        sem_wait(&ex.controle);
    }
    
    for(int i=0;i<nb_threads;i++){
        sem_post(&ex.attente[i]);
    }
}
