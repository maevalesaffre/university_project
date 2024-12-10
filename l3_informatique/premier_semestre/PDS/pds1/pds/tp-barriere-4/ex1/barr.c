#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include "answers.h"

struct barrier barr;

void fa(int i)
{
    printf("A(%d)\n", i);
}

void fb(int i)
{
    printf("B(%d)\n", i);
}

void *thread(void *arg)
{
    int index = *((int *)arg);
    fa(index);
    barr_synch(&barr);
    fb(index);
    return NULL;
}

int main(int argc, char *argv[])
{
    if (argc < 2) {
      printf("Spécifier le nombre de thread sur la ligne de commande\n");
      exit(-1);
    }
    int nthreads = atoi(argv[1]);

    pthread_t tid[nthreads];
    int index[nthreads];
    
    barr_init(&barr, nthreads);

    for (int i=0; i<nthreads; i++) {
        index[i] = i;
        pthread_create(&tid[i], 0, thread, &index[i]);
    }
    
    for (int i=0; i<nthreads; i++) {
        pthread_join(tid[i], 0);
    }
        
    return 0;
}
