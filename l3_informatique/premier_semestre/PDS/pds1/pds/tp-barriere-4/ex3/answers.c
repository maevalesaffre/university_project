#include "answers.h"
#include <stdlib.h>

void mbox_init(struct mailbox *mbox, int n)
{
    mbox->empty = malloc(sizeof(sem_t)*n);
    mbox->ncons = n;
    mbox->read = 0;
    for (int i=0; i<mbox->ncons; i++)
        sem_init(&mbox->empty[i], 0, 0);
    
    sem_init(&mbox->full, 0, 1);
    sem_init(&mbox->mutex, 0, 1);
}

void mbox_put(struct mailbox *mbox, int d)
{
    sem_wait(&mbox->full);
    sem_wait(&mbox->mutex);
    
    mbox->data = d;
    
    for (int i=0; i<mbox->ncons; i++)
        sem_post(&mbox->empty[i]);
    sem_post(&mbox->mutex);
}

int  mbox_get(struct mailbox *mbox, int index)
{
    int d;
    sem_wait(&mbox->empty[index]);
    sem_wait(&mbox->mutex);
    
    d = mbox->data;

    mbox->read++;
    if (mbox->read == mbox->ncons) {
        mbox->read = 0;
        sem_post(&mbox->full);
    }
    sem_post(&mbox->mutex);
    return d;
}


void mbox_destroy(struct mailbox *mbox)
{
    free(mbox->empty);
}
