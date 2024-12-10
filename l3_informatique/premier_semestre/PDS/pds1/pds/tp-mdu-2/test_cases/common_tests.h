/*************************************/
/** THIS FILE SHOULD NOT BE CHANGED **/
/*************************************/
#include <stdio.h>

#define ADD_POINT(n) output_note(argv[1], (n))

void output_note(const char* filename, int n);

void test_info(const char *info);
void test_passed(const char* test_name, const char* descr);
void test_failed(const char* test_name, const char* descr);
void test_failed_explain_int(const char* test_name, const char* descr, int exp, int obt);

int exec_and_parse_int(const char* cmd, int* error_occured);

#define TEST_CASE(TNAME, func1, func2, points) do {                     \
        int obt = func1;                                                \
        int exp = func2;                                                \
        if (obt == exp) {                                               \
            test_passed(TNAME, "--") ;                                  \
            ADD_POINT(points);                                          \
        }                                                               \
        else {                                                          \
            test_failed(TNAME, "--");                                 \
            printf("\tFile : %s Line : %d\n", __FILE__, __LINE__);       \
            printf("\tObtained => %d\n", obt);                          \
            printf("\tExpected => %d\n", exp);                          \
        }                                                               \
    }  while (0)
