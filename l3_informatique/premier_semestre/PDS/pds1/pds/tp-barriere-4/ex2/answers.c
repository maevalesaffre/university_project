#include <semaphore.h>
#include "answers.h"

sem_t sem[2];

void init()
{
    sem_init(&sem[0], 0, 0);
    sem_init(&sem[1], 0, 0);
}

void synch(int i)
{
    if (i>0) sem_post(&sem[i-1]);
    if (i<2) sem_wait(&sem[i]);
}
