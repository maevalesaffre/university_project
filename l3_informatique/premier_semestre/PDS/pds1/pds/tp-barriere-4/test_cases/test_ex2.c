#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include "../ex2/answers.h"
#include "logger.h"
#include "common_tests.h"

void fa(int i)
{
    usleep(100* (rand()%10) );
    tlog_log('A', i, 0);
}

void fb(int i)
{
    usleep(100* (rand()%10) );
    tlog_log('B', i, 0);
}


void *mythread(void *arg)
{
    int index = *((int *)arg);
    fa(index);
    synch(index);
    fb(index);
    return NULL;
}


int mytest(const char *filename, const char *testname)
{
    int nthreads = 3;
    pthread_t tid[nthreads];
    int index[nthreads];
    
    init();

    int result=1;
    for (int k = 0; k<30; k++) {
        // clear the log 
        tlog_clear();
        
        for (int i=0; i<nthreads; i++) {
            index[i] = i;
            pthread_create(&tid[i], NULL, mythread, &index[i]);
        }
        for (int i=0; i<nthreads; i++)
            pthread_join(tid[i], NULL);

        TASSERT(testname, tlog_check_before(tlog_s('A', 1, -1), tlog_s('B', 0, -1)),
                "Error : B(0) before A(1)", result);
        TASSERT(testname, tlog_check_before(tlog_s('A', 2, -1), tlog_s('B', 1, -1)),
                "Error : B(1) before A(2)", result);        
        usleep(100);
    }
    if (result) {
        test_passed(testname, "Check precedence");
        ADD_POINT(filename, testname, 3);
        return 1;
    }
    else {
        test_failed(testname, "Precedence not respected");
        return 0;
    }
    
}


int main(int argc, char *argv[])
{
    char *fname = "notes.txt";
    if (argc >= 2) fname = argv[1];
    
    int r = fork_test_and_wait(fname, "TestEx2", mytest, 2);
    exit(r);
}
