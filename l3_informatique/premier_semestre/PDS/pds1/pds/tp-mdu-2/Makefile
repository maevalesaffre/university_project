#######################################
### THIS FILE SHOULD NOT BE CHANGED ###
#######################################

CC=gcc
CFLAGS=-Wall -Wextra -fsanitize=address -Wno-unused-parameter
LDFLAGS=-pthread -fsanitize=address

EXE=prg
SRCS=$(wildcard *.c)
OBJS=$(SRCS:.c=.o)

TEST_SRCS=$(wildcard test_cases/*.c)
TEST_SRCS := $(filter-out test_cases/common_tests.c, $(TEST_SRCS))
TEST_OBJS=$(TEST_SRCS:.c=.o)
TEST_EXES=$(TEST_SRCS:.c=)

.PRECIOUS: %.o

.PHONY: clean test test-docker

$(EXE): $(OBJS)
	$(CC) $(LDFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

test_cases/%: test_cases/%.c answers.o test_cases/common_tests.o
	$(CC) $(CFLAGS) -c -o $@.o $<
	$(CC) $(LDFLAGS) -o $@ $@.o answers.o test_cases/common_tests.o

clean:
	@rm -f $(OBJS) $(EXE) $(TEST_OBJS) $(TEST_EXES) test_cases/common_tests.o
	@rm -rf test_cases/arbo test_cases/hello.txt test_cases/dir_sym

test: ${TEST_EXES}
	@./test_cases/run_tests.sh $(TEST_EXES)

test-docker:
	@docker build -q -t eval_pds_docker .
	@docker run --rm eval_pds_docker test
