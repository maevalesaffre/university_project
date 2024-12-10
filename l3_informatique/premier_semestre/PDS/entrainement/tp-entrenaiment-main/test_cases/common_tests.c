/*************************************/
/** THIS FILE SHOULD NOT BE CHANGED **/
/*************************************/

#include <stdio.h>

void output_note(const char* filename, int n) {
  FILE* f = NULL;
  // TODO : retry if already open
  f = fopen(filename, "a");
  if(f != NULL) {
    fprintf(f, "%i\n", n);
    fclose(f);
  }
}

void test_passed(const char* test_name, const char* descr) {
  printf("\033[;32mTest '%s': PASSED\033[0m\n\t%s\n", test_name, descr);
}

void test_failed(const char* test_name, const char* descr) {
  printf("\033[1;31mTest '%s': FAILED\033[0m\n\t%s\n", test_name, descr);
}
