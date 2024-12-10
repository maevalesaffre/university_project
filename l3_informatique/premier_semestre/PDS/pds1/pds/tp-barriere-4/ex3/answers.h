#pragma once

#include <semaphore.h>

struct mailbox {
    sem_t mutex;
    sem_t full;
    int data;
    int ncons;
    int read;
    sem_t *empty;
}; 

void mbox_init(struct mailbox *mbox, int n);
void mbox_put(struct mailbox *mbox, int d);
int  mbox_get(struct mailbox *mbox, int index);
void mbox_destroy(struct mailbox *mbox);
