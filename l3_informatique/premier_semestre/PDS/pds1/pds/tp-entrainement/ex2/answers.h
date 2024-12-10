/*************************************/
/** THIS FILE SHOULD NOT BE CHANGED **/
/*************************************/
#include <semaphore.h>

/* Exercice 2 */
struct barr_act {
    sem_t *s;
    sem_t c;
    sem_t m;
    int cont;
    int nbth;
};

void init(struct barr_act *b, int nb_threads);
void synch(struct barr_act *b, int index);
void activate(struct barr_act *b);
