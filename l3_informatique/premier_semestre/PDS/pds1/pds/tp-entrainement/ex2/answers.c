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

#include "answers.h"

/* Exercice 2 */

void init(struct barr_act *b, int nb_threads)
{
    b->cont = 0;
    b->nbth = nb_threads;
    b->s = (sem_t *)malloc(sizeof(sem_t)*nb_threads);
    for (int i=0; i<nb_threads; i++) sem_init(&b->s[i], 0, 0);
    sem_init(&b->c, 0, 0);
    sem_init(&b->m, 0, 1);
}

void synch(struct barr_act *b, int index)
{
    sem_wait(&b->m);
    b->cont++;
    if (b->cont == b->nbth) 
        sem_post(&b->c);
    
    sem_post(&b->m);
    sem_wait(&b->s[index]);
}

void activate(struct barr_act *b)
{
    sem_wait(&b->c);
    sem_wait(&b->m);
    b->cont = 0;
    for (int i=0; i<b->nbth; i++)
        sem_post(&b->s[i]);
    sem_post(&b->m);
}
