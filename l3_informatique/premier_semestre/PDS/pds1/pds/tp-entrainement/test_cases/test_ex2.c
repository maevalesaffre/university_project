/*************************************/
/** THIS FILE SHOULD NOT BE CHANGED **/
/*************************************/

#define _GNU_SOURCE

#include "testlib.h"
#include "tlogger.h"

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <pthread.h>
#include <signal.h>
#include <stdbool.h>

#include "../ex2/answers.h"

struct barr_act ba;

struct param {
    int index;
    int niter;
};

void *th(void *arg)
{
    struct param p = *((struct param *)arg);
    for (int i = 0; i<p.niter; i++) {
        usleep(100*(rand() % 3));
        tlog_log('T', p.index, i);
        synch(&ba, p.index);
    }
    return NULL;
}

void *ctrl(void *arg)
{
    struct param p = *((struct param *)arg);
    for (int i = 0; i<p.niter; i++) {
        usleep(100*(rand() % 3));
        activate(&ba);
        tlog_log('C', 0, i);
    }
    return NULL;
}

/* ------------------------------------ */

int niter = 2;
int nworkers = 1;
int npoints = 1; 

int test_gen(char *filename, char *tname)
{
    init(&ba, nworkers);

    pthread_t worker[nworkers];
    pthread_t control;
    
    struct param p[nworkers];

    tlog_clear();
  
    for (int i=0; i<nworkers; i++) {
        p[i].index = i;
        p[i].niter = niter;
        pthread_create(&worker[i], NULL, th, &p[i]);
    }
    pthread_create(&control, NULL, ctrl, &p[0]);

    for (int i=0; i<nworkers; i++) {
        pthread_join(worker[i], NULL);
    }
    pthread_join(control, NULL);

    int result = 1;

    for (int j=0; j<nworkers; j++) {
        TASSERT(tname,
                tlog_check_seq_n2('T', j, 0, niter),
                "Some work not executed",
                result);
    }
    
    for (int i=0; i<niter; i++) {
        for (int j=0; j<nworkers; j++) {
            TASSERT(tname,
                    tlog_check_before(tlog_s('T', j, i), tlog_s('C', 0, i)),
                    "Precedence not respected",
                    result);
        }
    }
    if (result) {
        test_passed(tname, "Two workers, 10 iterations");
        ADD_POINT(filename, tname, npoints);
    }
    return result;
}

int main(int argc, char* argv[]) {
    if(argc != 2) {
        printf("Usage : test1 <testfile>\n");
        return -1;
    }

    char *testfile = argv[1];

    niter = 2; nworkers = 1; npoints = 2;
    fork_test_and_wait(testfile, "BA1", test_gen, 4);
    niter = 10; nworkers = 1; npoints = 2;
    fork_test_and_wait(testfile, "BA2", test_gen, 4);
    niter = 2; nworkers = 10; npoints = 3;
    fork_test_and_wait(testfile, "BA3", test_gen, 4);
    niter = 10; nworkers = 10; npoints = 3;
    fork_test_and_wait(testfile, "BA4", test_gen, 4);
    
    return 0;
}
