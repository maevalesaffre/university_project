#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include "../ex3/answers.h"
#include "logger.h"
#include "common_tests.h"

struct mailbox mbox;

void Prod(int i)
{
    tlog_log('P', 0, i);
}

void Cons(int i, int d)
{
    tlog_log('C', i, d);
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

void test_ex3(int ncons)
{
    pthread_t prod_id;
    pthread_t cons_id[ncons];
    int indexes[ncons];
    
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
    return;
}


// 1 consumer
int mytest1(const char *fname, const char* tname)
{
    test_ex3(1);

    int r1 = 1, r2 = 2, r3 = 3, r4 = 4;
    // checks that all elements of P have been produced
    TASSERT(tname, tlog_check_seq_n2('P', 0, 0, 5),
            "Some element of P is missing", r1);
    // checks that C has obtained all elements
    TASSERT(tname, tlog_check_seq_n2('C', 0, 0, 5),
            "Some element of C is missing", r2);
    // checks if the producer was executed after the consumer
    for (int i=0; i<5; i++) {
        TASSERT(tname, tlog_check_before(tlog_s('P',0, i), tlog_s('C', 0, i)),
                "Consumer before producer?", r3);
    }
    // checks that the producer did not produce too quickly
    for (int i=0; i<3; i++) {
        TASSERT(tname, tlog_check_before(tlog_s('C', 0, i), tlog_s('P',0, i+2)),
                "Producer does not block correctly. More than one place in the mbox?", r4);
    }
    
    if (r1 && r2 && r3 && r4) {
        test_passed(tname, "The consumer has received all elements");
        ADD_POINT(fname, tname, 3);
        return 0;
    }
    else return 1;
}


// same for 3 consumers
int mytest3(const char *fname, const char* tname)
{
    test_ex3(3);
    int r1 = 1, r2 = 1, r3 = 1, r4 = 1;
    TASSERT(tname, tlog_check_seq_n2('P', 0, 0, 5),
            "Some element of P is missing", r1);
    
    for (int j=0; j<3 && r2; j++) {
        TASSERT(tname, tlog_check_seq_n2('C', j, 0, 5),
                "Some element of C is missing", r2);
    }
    for (int i=0; i<5 && r3; i++) {
        for (int j=0; j<3 && r3; j++) {
            TASSERT(tname, tlog_check_before(tlog_s('P',0, i), tlog_s('C', j, i)),
                    "Consumer before producer?", r3);
        }
    }
    
    for (int i=0; i<3 && r4; i++) {
        for (int j=0; j<3 && r4; j++) {
            TASSERT(tname, tlog_check_before(tlog_s('C', 0, i), tlog_s('P',0, i+2)),
                    "Producer does not block correctly. More than one place in the mbox?", r4);
        }
    }
    
    if (r1 && r2 && r3 && r4) {
        test_passed(tname, "The consumers have received all elements");
        ADD_POINT(fname, tname, 3);
        return 0;
    }        
    else return 1;

}

int main(int argc, char *argv[])
{
    char *fname = "notes.txt";
    if (argc >= 2) fname = argv[1];
       
    fork_test_and_wait(fname, "TestEx3_1", mytest1, 2);    
    fork_test_and_wait(fname, "TestEx3_3", mytest3, 3);

    return 0;
}
