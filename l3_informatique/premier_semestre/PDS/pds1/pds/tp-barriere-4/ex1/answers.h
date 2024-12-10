#pragma once

#include <semaphore.h>

struct barrier {
    sem_t s;
    sem_t m;
    int counter;
    int nthreads;
};

void barr_init(struct barrier *b, int n);
void barr_synch(struct barrier *b);
