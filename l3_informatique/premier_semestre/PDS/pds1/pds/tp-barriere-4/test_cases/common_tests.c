/*************************************/
/** THIS FILE SHOULD NOT BE CHANGED **/
/*************************************/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <signal.h>
#include <errno.h>
#include "common_tests.h"

void output_note(const char* filename, const char *exname, int n) {
  FILE* f = NULL;
  // TODO : retry if already open
  f = fopen(filename, "a");
  if(f != NULL) {
      fprintf(f, "%s=%i, ", exname, n);
    fclose(f);
  }
}


/* void output_note(const char* filename, int n) {
  FILE* f = NULL;
  // TODO : retry if already open
  f = fopen(filename, "a");
  if(f != NULL) {
    fprintf(f, "%i\n", n);
    fclose(f);
  }
  }*/

void test_info(const char* info) {
    printf("\t%s\n", info);
}


void test_passed(const char* test_name, const char* descr) {
  printf("\033[;32mTest '%s': PASSED\033[0m\n\t%s\n", test_name, descr);
}

void test_failed(const char* test_name, const char* descr) {
  printf("\033[1;31mTest '%s': FAILED\033[0m\n\t%s\n", test_name, descr);
}

void test_failed_explain_int(const char* test_name, const char* descr, int expected, int obtained) {
  printf("\033[1;31mTest '%s': FAILED\033[0m\n\t%s\n", test_name, descr);
  printf("\tExpected = %d\tObtained = %d\n", expected, obtained);
}


int exec_and_parse_int(const char* cmd, int* error_occured) {
  FILE* f;

  f = popen(cmd, "r");
  if(f != NULL) {
    int res;
    if(fscanf(f, "%i", &res) != EOF) {
      if(error_occured != NULL)
	*error_occured = 0;
      return res;
    }
  }

  if(error_occured != NULL)
    *error_occured = 1;
  return 0;
}

int fork_test_and_wait(const char *filename, const char *testname, test_fun fun, int tout)
{
    sigset_t mask;
    sigset_t orig_mask;
    struct timespec timeout;

    sigemptyset (&mask);
    sigaddset (&mask, SIGCHLD);

    if (sigprocmask(SIG_BLOCK, &mask, &orig_mask) < 0) {
        perror ("sigprocmask");
        return 1;
    }
    
    pid_t pid = fork();
    if (pid == 0) {
        fun(filename, testname);
        exit(0);
    }
    
    timeout.tv_sec = tout;
    timeout.tv_nsec = 0;
    
    do {
        if (sigtimedwait(&mask, NULL, &timeout) < 0) {
            if (errno == EINTR) {
                /* Interrupted by a signal other than SIGCHLD. */
                continue;
            }
            else if (errno == EAGAIN) {
                test_failed(testname, "--");                 
                printf ("Timeout, killing child\n");
                kill (pid, SIGKILL);
            }
            else {
                perror ("sigtimedwait");
                return 1;
            }
        }
         
        break;
    } while (1);
     
    if (waitpid(pid, NULL, 0) < 0) {
        perror ("waitpid");
        return 1;
    }
    return 0;
}
