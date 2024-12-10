#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include "../ex1/answers.h"
#include "logger.h"
#include "common_tests.h"

struct barrier barr;
    
void *mythread(void *arg)
{
    int index = *((int *)arg);
    
    usleep(100* (rand()%10) );
    tlog_log('A', index, 0);
    barr_synch(&barr);
    usleep(100* (rand()%10) );
    tlog_log('B', index, 0);
    
    return NULL;
}


int test(const char *fname, const char *tname)
{
    int nthreads = 3;

    pthread_t tid[nthreads];
    int index[nthreads];
    
    int result = 1;
    for (int k = 0; k<30 && result; k++) {

        barr_init(&barr, nthreads);
        // clear the log 
        tlog_clear();
        
        for (int i=0; i<nthreads; i++)  {
            index[i] = i;
            pthread_create(&tid[i], NULL, mythread, &index[i]);
        }
        
        for (int i=0; i<nthreads; i++)
            pthread_join(tid[i], NULL);

        // after all threads have completed, check that all 'A's are before all 'B's
        TASSERT(tname, tlog_check_before(tlog_s('A', -1, 0),
                                         tlog_s('B', -1, 0)),
                "Precedence not respected",
                result);
        
        usleep(100);
    }
    if (result) {
        test_passed(tname, "Check precedence");
        ADD_POINT(fname, tname, 3);
    }
    else 
        test_failed(tname, "Precedence not respected");
    return 0;
}


int main(int argc, char *argv[])
{
    char *fname = "notes.txt";
    if (argc >= 2) fname = argv[1];
    
    fork_test_and_wait(fname, "TestEx1", test, 2);
}
