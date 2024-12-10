#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include "answers.h"

struct mailbox mbox;

void Prod(int i)
{
    printf("Prod(%d)\n", i);
}

void Cons(int i, int d)
{
    printf("Cons(%d,%d)\n", i, d);
}

void *producteur(void *arg)
{
    for (int i=0; i<5; i++) {
        Prod(i);
        mbox_put(&mbox, i);
    }
    return NULL;
}

void *consommateur(void *arg)
{
    int index = *((int *)arg);

    for (int i=0; i<5; i++) {
        int d = mbox_get(&mbox, index);
        Cons(index, d);
    }
    return NULL;
}


int main(int argc, char *argv[])
{
    if (argc < 2) {
        printf("  Usage : %s num_cons\n  with num_cons > 0\n", argv[0]);
        exit(1);
    }
    int ncons = atoi(argv[1]);
    if (ncons < 1) {
        printf("ncons should be a positive number\n");
        exit(1);
    }
    pthread_t prod_id;
    pthread_t cons_id[ncons];
    int indexes[ncons];

    printf("Mbox with 1 producer and %d consumers\n", ncons);
    
    mbox_init(&mbox, ncons);
    
    for (int i = 0; i<ncons; i++) {
        indexes[i] = i;
        pthread_create(&cons_id[i], 0, consommateur, (void*)&indexes[i]);
    }
    pthread_create(&prod_id, 0, producteur, 0);

    for (int i=0; i<ncons; i++)
        pthread_join(cons_id[i], 0);

    pthread_join(prod_id, 0);

    mbox_destroy(&mbox);
    
    return 0;
}
