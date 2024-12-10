/*************************************/
/** THIS FILE SHOULD NOT BE CHANGED **/
/*************************************/

#define ADD_POINT(n) output_note(argv[1], (n))

void output_note(const char* filename, int n);

void test_passed(const char* test_name, const char* descr);
void test_failed(const char* test_name, const char* descr);
