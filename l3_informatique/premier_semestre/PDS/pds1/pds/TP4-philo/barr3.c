#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

void fa(int i)
{
    printf("A(%d)\n", i);
}

void fb(int i)
{
    printf("B(%d)\n", i);
}

void synch(int i)
{
    //TODO
    
    printf("S(%d)\n", i);
}


void *thread(void *arg)
{
    int index = (int)arg;
    fa(index);
    synch(index);
    fb(index);
    return NULL;
}



int main()
{
    pthread_t tid[3];

    printf("In the main\n");
    for (int i=0; i<3; i++) 
        pthread_create(&tid[i], NULL, thread, (void *)i);

    for (int i=0; i<3; i++) 
        pthread_join(tid[i], NULL);
    
    printf("END\n");
    return 0;
}
