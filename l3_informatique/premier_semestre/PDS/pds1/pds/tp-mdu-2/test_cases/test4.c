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

    opt_follow_links = 1;
    opt_apparent_size = 0;

    test_info("Setting opt_follow_links = 1 and opt_apparent_size = 0\n");
    
    TEST_CASE("Ex 4 - file",
              du_file("test_cases/hello.txt"),
              exec_and_parse_int("stat -Lc '%b' test_cases/hello.txt", NULL),
              1);
    
    TEST_CASE("Ex 4 - link",
              du_file("test_cases/arbo/link"),
              exec_and_parse_int("stat -Lc '%b' test_cases/arbo/link", NULL),
              1);

    TEST_CASE("Ex 4 - dir link",
              is_dir("test_cases/dir_sym"),
              1,
              1);
    
    TEST_CASE("Ex 4 - arborescence",
              du_file("test_cases/arbo"),
              exec_and_parse_int("du -L --block-size 512 -s test_cases/arbo", NULL),
              1);
    
    return 0;
  }

  else if(p > 0) {
    int wstatus;

    waitpid(p, &wstatus, 0);

    if(!WIFEXITED(wstatus)) {
      test_failed("Ex4 - Segfault", "Segfault en testant l'exercice 4");
    }
  }

  return 0;
}
