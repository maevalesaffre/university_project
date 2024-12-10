#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

// Définir les structures de données nécessaires à la synchronisation.  

void barr_synch()
{
    // TODO
}

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
    int index = (int)arg;
    fa(index);
    barr_synch();
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

    // TODO
    // Créez les threads et attendez leur terminaison
}
