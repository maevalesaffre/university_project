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
        int s; int exp;

        opt_follow_links = 0;
        opt_apparent_size = 0;

        TEST_CASE("Ex 1 - file",
                  du_single_file("test_cases/hello.txt"),
                  exec_and_parse_int("stat -c '%b' test_cases/hello.txt", NULL),
                  2);

        TEST_CASE("Ex 1 - link",
                  du_single_file("test_cases/arbo/link"),
                  exec_and_parse_int("stat -c '%b' test_cases/arbo/link", NULL),
                  1);
    

        TEST_CASE("Ex 1 - err",
                  du_single_file("test_cases/sdnqjfkdnfjkazekjnzjkatjkeza"),
                  -1,
                  1);
    
        return 0;
    }
    else if(p > 0) {
        int wstatus;

        waitpid(p, &wstatus, 0);

        if(!WIFEXITED(wstatus)) {
            test_failed("Ex1 - Segfault", "Segfault en testant l'exercice 1");
        }
    }

    return 0;
}
