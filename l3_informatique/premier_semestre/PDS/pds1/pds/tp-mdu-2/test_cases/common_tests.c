/*************************************/
/** THIS FILE SHOULD NOT BE CHANGED **/
/*************************************/

#include <stdio.h>
#include <stdlib.h>

void output_note(const char* filename, int n) {
  FILE* f = NULL;
  // TODO : retry if already open
  f = fopen(filename, "a");
  if(f != NULL) {
    fprintf(f, "%i\n", n);
    fclose(f);
  }
}

void test_info(const char* info) {
    printf("\t%s\n", info);
}


void test_passed(const char* test_name, const char* descr) {
  printf("\033[;32mTest '%s': PASSED\033[0m\n\t%s\n", test_name, descr);
}

void test_failed(const char* test_name, const char* descr) {
  printf("\033[1;31mTest '%s': FAILED\033[0m\n\t%s\n", test_name, descr);
}

void test_failed_explain_int(const char* test_name, const char* descr, int expected, int obtained) {
  printf("\033[1;31mTest '%s': FAILED\033[0m\n\t%s\n", test_name, descr);
  printf("\tExpected = %d\tObtained = %d\n", expected, obtained);
}


int exec_and_parse_int(const char* cmd, int* error_occured) {
  FILE* f;

  f = popen(cmd, "r");
  if(f != NULL) {
    int res;
    if(fscanf(f, "%i", &res) != EOF) {
      if(error_occured != NULL)
	*error_occured = 0;
      return res;
    }
  }

  if(error_occured != NULL)
    *error_occured = 1;
  return 0;
}
