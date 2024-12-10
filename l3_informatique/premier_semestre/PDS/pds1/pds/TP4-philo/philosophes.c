#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

#define N 4 

// TODO : declarer les semaphores
struct fork{
    sem_t dispo[N];
    sem_t mutex[N];
    int taken[N];
};
struct fork forks;

int fork_left(int fn)
{
    return fn;
}

int fork_right(int fn)
{
    return (fn+1)%N;
}

int take_fork(int fork_number, int other_fork)
{
    // TODO 
    sem_wait(&forks.mutex[fork_number]);
    while(&forks.taken[fork_number] == 0 && &forks.taken[other_fork] == 0){        
        sem_wait(&forks.dispo[fork_number]);
        forks.taken[fork_number]=1;        
    }
    
    return 0;
}

void leave_fork(int fork_number)
{
    // TODO
    forks.taken[fork_number]=0;
    sem_post(&forks.dispo[fork_number]);
    sem_post(&forks.mutex[fork_number]);
    return;
}

void think(int phi)
{
    printf("Philosophe %d pense...\n", phi);
    sleep(rand()%5);
    printf("Philosophe %d a faim !\n", phi);
}

void eat(int phi)
{
    printf("Philosophe %d mange\n", phi);
    sleep(rand()%2);
    printf("Philosophe %d a terminé\n", phi);
}

void *philosophe(void *arg)
{
    int index = (int) arg;

    for (int i=0; i<10; i++) {
        think(index);
        take_fork(fork_left(index),fork_right(index));
        take_fork(fork_right(index),fork_left(index));
        eat(index);
        leave_fork(fork_right(index));
        leave_fork(fork_left(index));
    }
    return NULL;
}

void initSem(){
    for(int i=0; i<N;i++){
        sem_init(&forks.dispo[i],0,1);
        sem_init(&forks.mutex[i],0,1);
        forks.taken[i]=0;
    }
}

int main()
{
    pthread_t tid[N];

    // TODO: Creer des structures de données pour la syncrhonisations
    
    initSem();

    for (int i=0; i<N; i++)
        pthread_create(&tid[i], 0, philosophe, (void *)i);

    for (int i=0; i<N; i++)
        pthread_join(tid[i], 0);
    return 0;
}


