#include "answers.h"
#include <semaphore.h>

void barr_init(struct barrier *b, int n)
{
    b->nthreads = n;
    sem_init(&b->s, 0, 0);
    sem_init(&b->m, 0, 1);
    b->counter = 0;
}

void barr_synch(struct barrier *b)
{
    sem_wait(&b->m);
    b->counter++;
    if (b->counter == b->nthreads) {
        for (int i=0; i < b->nthreads-1; i++)
            sem_post(&b->s);
        b->counter = 0;
        sem_post(&b->m);
    }
    else {
        sem_post(&b->m);
        sem_wait(&b->s);
    }
}

