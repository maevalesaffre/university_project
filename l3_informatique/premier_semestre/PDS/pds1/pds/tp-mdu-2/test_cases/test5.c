/*************************************/
/** THIS FILE SHOULD NOT BE CHANGED **/
/*************************************/

#include "../answers.h"
#include "common_tests.h"

#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main(int argc, char* argv[]) {
  if(argc != 2)
    return -1;

  // Run test in an other process to catch segfaults
  pid_t p = fork();
  if(p == 0) {

    opt_follow_links = 0;
    opt_apparent_size = 1;

    TEST_CASE("Ex 5 - file",
              du_file("test_cases/hello.txt"),
              exec_and_parse_int("stat -c '%s' test_cases/hello.txt", NULL),
              1);
    
    TEST_CASE("Ex 5 - link",
              du_file("test_cases/arbo/link"),
              exec_and_parse_int("stat -c '%s' test_cases/arbo/link", NULL),
              1);

    TEST_CASE("Ex 5 - arborescence",
              du_file("test_cases/arbo"),
              exec_and_parse_int("du --apparent-size --block-size 1 -s test_cases/arbo", NULL),
              2);

    return 0;
  }

  else if(p > 0) {
    int wstatus;

    waitpid(p, &wstatus, 0);

    if(!WIFEXITED(wstatus)) {
      test_failed("Ex5 - Segfault", "Segfault en testant l'exercice 5");
    }
  }

  return 0;
}
