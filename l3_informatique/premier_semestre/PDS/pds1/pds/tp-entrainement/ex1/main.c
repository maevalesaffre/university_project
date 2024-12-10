#include "answers.h"

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <pthread.h>

#define NTHREADS 3

void affiche_str(char* string) {
  printf("%s\n", string);
}

int main(int argc, char* argv[]) {

  /* Main exercice 1 */
  if(argc != 2) {
    printf("usage: %s dirname\n", argv[0]);
    exit(-1);
  }
  liste_sous_reps(argv[1]);

  return 0;
}
