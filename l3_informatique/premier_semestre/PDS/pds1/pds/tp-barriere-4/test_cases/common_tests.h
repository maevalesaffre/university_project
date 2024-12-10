/*************************************/
/** THIS FILE SHOULD NOT BE CHANGED **/
/*************************************/
#include <stdio.h>

/**
   Prototype of a testing function:
   - takes as input the filename and the test name.
   - returns 0 if everything is ok, 1 if some test has failed. 
 */
typedef int (*test_fun)(const char *filename, const char *name);


/**
   Write the points on the file.
   The file is a comma separated list of couples

   tname=point

   and can be easily parsed later to collect all the points
*/     
void output_note(const char* filename, const char* testname, int n);

/**
   Prints infos on the screen
*/
void test_info(const char *info);
/**
   To be called if the test has been succesfully passed to inform the
   user that the test has passed.
 */
void test_passed(const char *test_name, const char *descr);

/**
   To be called if the test has failed to inform the user.
 */
void test_failed(const char *test_name, const char *descr);

/**
   To be called if the test has faild to inform the user,
   it prints the difference between the expected value and the obtained value. 
 */
void test_failed_explain_int(const char* test_name, const char* descr, int exp, int obt);

/**
   Executed the external command "cmd", waits for it to finish, and
   returns the obtained value.
 */
int exec_and_parse_int(const char* cmd, int* error_occured);

/**
   For a test in an external process, and waits for it. It is possible
   to specify a timeout (tout), if the process does not terminate
   before the timeout exprires, it returns an error.

   The test function takes the test file and the test name as
   parameters.
 */
int fork_test_and_wait(const char *filemane, const char *testname, test_fun fun, int tout);

/**
   Macro to compare two results.
   - FNAME: name of the file where the points are marked
   - TNAME: name of the test
   - func1: function to call, or expression;
   - func2: function to call, of expression;
   - how many points this test will give
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




