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

void affiche_str(char* string) {}

bool th1_end = false;
void *th1(__attribute__((unused)) void *arg) {
  synch(0);
  th1_end = true;
  return NULL;
}

bool th2_end = false;
void *th2(__attribute__((unused)) void *arg) {
  synch(1);
  th2_end = true;
  return NULL;
}

bool th3_end = false;
void *th3(__attribute__((unused)) void *arg) {
  synch(2);
  th3_end = true;
  return NULL;
}

bool th4_end = false;
void *th4(__attribute__((unused)) void *arg) {
  synch(3);
  th4_end = true;
  return NULL;
}

bool th5_end = false;
void *th5(__attribute__((unused)) void *arg) {
  synch(4);
  th5_end = true;
  return NULL;
}

bool ctrl_end = false;
void *ctrl_func(__attribute__((unused)) void *arg) {
  activate(5);
  ctrl_end = true;
  return NULL;
}

int end() {
  printf("\033[1;31m\tTest failed\033[0m\n");
  return 0;
}

int main(int argc, char* argv[]) {
  if(argc != 2)
    return -1;

  printf("Running exercice 2 with 5 threads, various scenario\n");

  srand(time(NULL));

  pthread_t t1, t2, t3, t4, t5, ctrl;

  init(5);

  /* First loop */
  pthread_create(&t1, NULL, th1, NULL);pthread_detach(t1);
  pthread_create(&t2, NULL, th2, NULL);pthread_detach(t2);
  pthread_create(&t3, NULL, th3, NULL);pthread_detach(t3);
  pthread_create(&t4, NULL, th4, NULL);pthread_detach(t4);
  pthread_create(&t5, NULL, th5, NULL);pthread_detach(t5);
  pthread_create(&ctrl, NULL, ctrl_func, NULL);pthread_detach(ctrl);

  sleep(1 + rand()%2);

  if(!th1_end) {return end();}
  if(!th2_end) {return end();}
  if(!th3_end) {return end();}
  if(!th4_end) {return end();}
  if(!th5_end) {return end();}
  if(!ctrl_end) {return end();}

  /* Second loop */
  th1_end = false; pthread_create(&t1, NULL, th1, NULL);pthread_detach(t1);
  ctrl_end = false; pthread_create(&ctrl, NULL, ctrl_func, NULL);pthread_detach(ctrl);
  th2_end = false; pthread_create(&t2, NULL, th2, NULL);pthread_detach(t2);
  th5_end = false; pthread_create(&t5, NULL, th5, NULL);pthread_detach(t5);
  th3_end = false; pthread_create(&t3, NULL, th3, NULL);pthread_detach(t3);
  th4_end = false; pthread_create(&t4, NULL, th4, NULL);pthread_detach(t4);

  sleep(1 + rand()%2);

  if(!th1_end) {return end();}
  if(!th2_end) {return end();}
  if(!th3_end) {return end();}
  if(!th4_end) {return end();}
  if(!th5_end) {return end();}
  if(!ctrl_end) {return end();}

  /* Third loop */
  th1_end = false; pthread_create(&t1, NULL, th1, NULL);pthread_detach(t1);
  th2_end = false; pthread_create(&t2, NULL, th2, NULL);pthread_detach(t2);
  th3_end = false; pthread_create(&t3, NULL, th3, NULL);pthread_detach(t3);
  th4_end = false; pthread_create(&t4, NULL, th4, NULL);pthread_detach(t4);
  ctrl_end = false; pthread_create(&ctrl, NULL, ctrl_func, NULL);pthread_detach(ctrl);

  sleep(1 + rand()%2);

  if(th1_end) {return end();}
  if(th2_end) {return end();}
  if(th3_end) {return end();}
  if(th4_end) {return end();}
  if(ctrl_end) {return end();}

  th5_end = false; pthread_create(&t5, NULL, th5, NULL);pthread_detach(t5);
 
  sleep(1 + rand()%2);

  if(!th1_end) {return end();}
  if(!th2_end) {return end();}
  if(!th3_end) {return end();}
  if(!th4_end) {return end();}
  if(!th5_end) {return end();}
  if(!ctrl_end) {return end();}

  /* End of the test */
  printf("\033[;32m\tTest OK\033[0m\n");
  ADD_POINT(3);

  return 0;
}
