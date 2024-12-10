/*************************************/
/** THIS FILE SHOULD NOT BE CHANGED **/
/*************************************/

#define _GNU_SOURCE

#include "../answers.h"
#include "common_tests.h"

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <pthread.h>
#include <stdbool.h>
#include <signal.h>
#include <stdbool.h>

void affiche_str(char* string) {}

bool th1_end = false;
void *th1(__attribute__((unused)) void *arg) {
  nice(-19);
  synch(0);
  synch(0);
  th1_end = true;
  return NULL;
}

bool th2_end = false;
void *th2(__attribute__((unused)) void *arg) {
  nice(19);
  synch(1);
  synch(1);
  th2_end = true;
  return NULL;
}

bool ctrl_end = false;
void *ctrl_func(__attribute__((unused)) void *arg) {
  activate(2);
  ctrl_end = true;
  return NULL;
}

int main(int argc, char* argv[]) {
  if(argc != 2)
    return -1;

  printf("Running exercice 2 with 2 threads, synch(0)&synch(0) | synch(1)&synch(1) | activate(2)\n");

  srand(time(NULL));

  pthread_t t1, t2, ctrl;
  bool failed = false;

  init(3);

  th1_end = false; pthread_create(&t1, NULL, th1, NULL); pthread_detach(t1);
  th2_end = false; pthread_create(&t2, NULL, th2, NULL); pthread_detach(t2);
  ctrl_end = false; pthread_create(&ctrl, NULL, ctrl_func, NULL); pthread_detach(ctrl);

  sleep(1);  

  if(th1_end) {
    printf("\033[1;31m\tSecond synch(0) returned\033[0m\n");
    failed = true;
  }

  if(th2_end) {
    printf("\033[1;31m\tSecond synch(1) returned\033[0m\n");
    failed = true;
  }

  if(!ctrl_end) {
    printf("\033[1;31m\tActivate(2) never ends\033[0m\n");
    failed = true;
  }

  if(!failed) {
    printf("\033[;32m\tTest OK\033[0m\n");    
    ADD_POINT(3);
  }
  
  return 0;
}
