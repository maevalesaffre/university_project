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
    opt_apparent_size = 0;

    TEST_CASE("Ex 2 - file", 
              is_dir("test_cases/arbo/subdir/data.txt"),
              0,
              1);
        
    TEST_CASE("Ex 2 - dir",
              is_dir("test_cases/arbo/subdir"),
              1,
              1);

    TEST_CASE("Ex 2 - err",
              (is_dir("ezarlkreakl") == -1) && (is_dir("test_cases/arbo/subdir/data.txt/") == -1),
              1,
              1);

    TEST_CASE("Ex 2 - slash",
              (is_dir("test_cases/arbo/subdir/") == 1 && is_dir("test_cases/arbo/subdir/data.txt/") == -1),
              1,
              1);

    return 0;
  }

  else if(p > 0) {
    int wstatus;

    waitpid(p, &wstatus, 0);

    if(!WIFEXITED(wstatus)) {
      test_failed("Ex2 - Segfault", "Segfault en testant l'exercice 2");
    }
  }

  return 0;
}
