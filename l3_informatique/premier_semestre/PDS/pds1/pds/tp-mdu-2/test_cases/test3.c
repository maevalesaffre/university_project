/*************************************/
/** THIS FILE SHOULD NOT BE CHANGED **/
/*************************************/

#include "../answers.h"
#include "common_tests.h"

#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char* argv[]) {
  if(argc != 2)
    return -1;

  // Run test in an other process to catch segfaults
  pid_t p = fork();
  if(p == 0) {
    opt_follow_links = 0;
    opt_apparent_size = 0;

    TEST_CASE("Ex 3 - arborescence", 
              du_file("test_cases/arbo"),
              exec_and_parse_int("du --block-size 512 -s test_cases/arbo", NULL),
              2);
    

    TEST_CASE("Ex 3 - file",
              du_file("test_cases/arbo/subdir/data2.txt"),
              exec_and_parse_int("du --block-size 512 -s test_cases/arbo/subdir/data2.txt", NULL),
              1);

    opt_apparent_size = 0;
    TEST_CASE("Ex 3 - link",
              du_file("test_cases/arbo/link"),
              exec_and_parse_int("du --block-size 512 -s test_cases/arbo/link", NULL),
              1);
    
    return 0;
  }

  else if(p > 0) {
    int wstatus;

    waitpid(p, &wstatus, 0);

    if(!WIFEXITED(wstatus)) {
      test_failed("Ex3 - Segfault", "Segfault en testant l'exercice 3");
    }
  }

  return 0;
}
