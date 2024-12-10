#pragma once

#include <stdio.h>

/**
   Prototype of a testing function:
   - takes as input the name of the file where the test results
     will be stored, and the name of this test
   - returns 0 if everything is ok, 1 if some assertion has failed. 
 */
typedef int (*test_fun)(char *filename, char *name);

/**
   Write the points on the file.
   The file will contain a comma-separated list of couples 'tname=point'
*/     
void output_note(const char* filename, const char* testname, int n);

/**
   Prints infos on the screen
*/
void test_info(const char *info);

/**
   To be called if the test has been succesfully passed to inform the
   user.
 */
void test_passed(const char *test_name, const char *descr);

/**
   To be called if the test has failed to inform the user.
*/
void test_failed(const char *test_name, const char *descr);

/**
   To be called if the test has failed to inform the user,
   it prints the difference between the expected value and the obtained value. 
 */
void test_failed_explain_int(const char* test_name, const char* descr, int exp, int obt);

/**
   Executes the external command "cmd", waits for it to finish, and
   returns the obtained value.
 */
int exec_and_parse_int(const char* cmd, int* error_occured);

/**
   For a test in an external process, and waits for it. It is possible
   to specify a timeout (tout): if the process does not terminate
   before the timeout expires, it returns an error.

   The test function takes the test file and the test name as
   parameters.
 */
int fork_test_and_wait(const char *filemane, const char *testname, test_fun fun, int tout);

/**
   Macro to compare two results.
   - FNAME: name of the file where the points are marked
   - TNAME: name of the test
   - func1: function or expression;
   - func2: function or expression;
   - how many points this test will give if succesfull
 */
#define TEST_EQ(FNAME, TNAME, func1, func2, points) do {                \
        int obt = (func1);                                              \
        int exp = (func2);                                              \
        if (obt == exp) {                                               \
            test_passed(TNAME, "--") ;                                  \
            ADD_POINT(FNAME, TNAME, points);                            \
        }                                                               \
        else {                                                          \
            test_failed(TNAME, "--");                                   \
            printf("\tFile : %s Line : %d\n", __FILE__, __LINE__);      \
            printf("\tObtained => %d\n", obt);                          \
            printf("\tExpected => %d\n", exp);                          \
        }                                                               \
    }  while (0)

/**
   Adds n points for the test t
 */
#define ADD_POINT(file, t, n) output_note(file, (t), (n))

/**
   Helper function to remove consecutive slashes from a pathname.

   It replaces the string in place.
*/
void remove_double_slash(char *string);

