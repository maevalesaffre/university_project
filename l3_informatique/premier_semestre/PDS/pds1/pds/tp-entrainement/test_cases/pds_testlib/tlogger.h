#pragma once

#include "testlib.h"

#define MAX_LOGS 1000
#define ERRMSG_LEN 1024

/**
  The log entry.

  - id : a character. Typically used to identify the thread
        (e.g. 'P' as producer, 'C' as consumer) ;
        '*' matches "any" character in searches and comparisons.
  - n1 : a non-negative integer.
         Typically used as the index of the thread.
         A negative number matches "any" positive number in searches
         and comparisons.
  - n2 : a non-negative number. Typically, it indicates
         the operation.
         A negative number matches "any" positive number in searches
         and comparisons.
*/
typedef struct tlog_entry {
    char id;
    int n1;
    int n2;
} tlog_entry;

/**
  A convenience function to create a structure tlog_entry.
  - a cannot be '*';
  - b and c cannot be negative.
 */
tlog_entry tlog_s(char a, int b, int c);

/**
   Logs an entry.
   The threads will call this during their execution. It uses atomic operations
   to protect the log array. 
*/
void tlog_log(char id, int n1, int n2);

/**
   Clears the logs.
*/
void tlog_clear();

/**
   Prints all entries so far on stdout. 
 */
void tlog_print();

/**
   Returns the last error message. This is supposed to be called after
   the threads have completed execution. If you call it before,
   results are unpredictable.
 */
char *tlog_last_error_msg();

/**
   Checks if entry e is present in the log.
 */
int tlog_exists(tlog_entry e);

/**
    Check precedence constraints between two entries.

    Returns 1 if :
    - neither (b, b_n1, b_n2) nor (a, a_n1, a_n2) can
      be found in the logs.
    - if (a, a_n1, a_n2) exists and (b, b_n1, b_n2) comes after;
    Return 0 otherwise.

    Example :

       tlog_check_before(tlog_s('A', 0, 1) , tlog_s('B', 0, 1));

    returns 1 if the operation ('A', 0, 1) has been done
    before operation ('B', 0, 1).

    Wildcards are possible : '*' for the first field, a negative integer
    for the other two parameters.

    Example:

       tlog_check_before(tlog_s('A', -1, -1) , tlog_s('B', -1, -1));

    checks that all 'A's appear before all 'B's (typically, to check a barrier).
*/
int tlog_check_before(struct tlog_entry before, struct tlog_entry after);

/**
    Checks that all elements (id, n, n2) are present in any order,
    with n in [n1_min....n1_max-1]

    NO WILDCARDS!
*/
int tlog_check_all_n1(char id, int n1_min, int n1_max, int n2);

/**
    Checks that all elements (id, n1, n) are present in any order,
    with n2 in [n2_min....n2_max-1]

    NO WILDCARDS!
*/
int tlog_check_all_n2(char id, int n1, int n2_min, int n2_max);

/**
    Checks that all elements (id, n1, n) are present in incrementing order,
    with n in [n2_min....n2_max-1]

    NO WILDCARDS!
*/
int tlog_check_seq_n2(char id, int n1, int n2_min, int n2_max);

/** Macro to assert a property */
#define TASSERT(TNAME, prop, errmsg, result) do {                       \
        if (!(prop)) {                                                  \
            test_failed(TNAME, "--");                                   \
            printf("\033[1;31m[FAIL] file %s, line: %d\033[0m\n", __FILE__, __LINE__); \
            printf("Error : %s\n", errmsg);                             \
            tlog_print();                                               \
            result = 0;                                                 \
        }                                                               \
        else {                                                          \
            result = result && 1;                                       \
        }                                                               \
    } while (0)


