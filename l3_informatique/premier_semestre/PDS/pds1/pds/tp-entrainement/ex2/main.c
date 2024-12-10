#include "answers.h"

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <pthread.h>

#define NTHREADS 3

struct barr_act ba;

void w(int tid, int step)
{
    printf("W(%d) STEP %d\n", tid, step);
}

void *thread(void *arg)
{
    long index = (long) arg;

    for (int i = 0; i<10; i++) {
        w(index, i);
        synch(&ba, index);
    }
    return NULL;
}

void *control(void *arg)
{
    for (int i=0; i<10; i++) {
        printf("Waiting for completing step %d\n", i);
        activate(&ba);
    }
    return NULL;
}

int main(int argc, char* argv[])
{
    /* Main exercice 2 */
    pthread_t tid[NTHREADS];
    pthread_t control_tid;

    init(&ba, NTHREADS);
    
    for (long i=0; i<NTHREADS; i++) 
        pthread_create(&tid[i], 0, thread, (void *) i);
    pthread_create(&control_tid, 0, control, 0);
  
    for (int i=0; i<NTHREADS; i++)
        pthread_join(tid[i], 0);
    pthread_join(control_tid, 0);
  
    return 0;
}
