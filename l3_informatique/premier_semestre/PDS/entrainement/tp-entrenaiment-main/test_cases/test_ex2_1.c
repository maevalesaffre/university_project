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
#include <signal.h>
#include <stdbool.h>

void affiche_str(char* string) {}

bool th1_end = false;
void *th1(__attribute__((unused)) void *arg) {
  synch(0);
  th1_end = true;
  return NULL;
}

bool ctrl_end = false;
void *ctrl_func(__attribute__((unused)) void *arg) {
  activate(1);
  ctrl_end = true;
  return NULL;
}

int main(int argc, char* argv[]) {
  if(argc != 2)
    return -1;

  printf("Running exercice 2 with 1 thread, synch(0) then activate(1)\n");

  srand(time(NULL));

  pthread_t t1, ctrl;

  init(1);

  pthread_create(&t1, NULL, th1, NULL); pthread_detach(t1);
  sleep(1+rand()%2);

  if(th1_end) {
    printf("\033[1;31m\tSynch(0) doesn't wait for activate\033[0m\n");
  } else {

    pthread_create(&ctrl, NULL, ctrl_func, NULL); pthread_detach(ctrl);
    sleep(1);

    if(th1_end) {
      if(ctrl_end) {
	printf("\033[;32m\tTest OK\033[0m\n");
	ADD_POINT(1);
      } else {
	printf("\033[1;31m\tActivate(1) never ends\033[0m\n");
      }
    } else {
      printf("\033[1;31m\tSynch(0) never ends\033[0m\n");
    }
  }

  return 0;
}
