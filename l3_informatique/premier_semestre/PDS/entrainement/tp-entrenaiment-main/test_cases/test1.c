/*************************************/
/** THIS FILE SHOULD NOT BE CHANGED **/
/*************************************/

#include "../answers.h"
#include "common_tests.h"

#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

#define NB_EXPECTED 0
char* expected_str[NB_EXPECTED] = {};
bool found[NB_EXPECTED] = {};
bool failed = false;

void affiche_str(char* string) {
  bool is_expected = false;

  for(int i=0; i<NB_EXPECTED ; i++) {
    if(!strcmp(string, expected_str[i])) {
      is_expected = true;
      if(found[i] == true) {
	printf("\033[1;31m\t%s printed several times\033[0m\n", expected_str[i]);
	failed = true;
      } else
	found[i] = true;
    }
  }

  if(!is_expected) {
    printf("\033[1;31m\t%s should not be printed\033[0m\n", string);
	failed = true;
  }
}

int main(int argc, char* argv[]) {
  if(argc != 2)
    return -1;

  printf("Running exercice 1 on \"test_cases/arbo_test1/\"\n");

  pid_t p = fork();
  if(p == 0) {
    liste_sous_reps("test_cases/arbo_test1/");
    bool all_found = true;

    for(int i=0; i<NB_EXPECTED ; i++) {
      if(!found[i]) {
	all_found = false;
	printf("\033[1;31m\t%s is missing\033[0m\n", expected_str[i]);
	failed = true;
      }
    }

    if(all_found && !failed) {
      printf("\033[;32m\tTest OK\033[0m\n");
      ADD_POINT(1);
    }

    return 0;
  }

  else if(p > 0) {
    int wstatus;

    waitpid(p, &wstatus, 0);

    if(!WIFEXITED(wstatus)) {
      printf("\033[1;31m\tTest crashed\033[0m\n");
    }
  }

  return 0;
}
