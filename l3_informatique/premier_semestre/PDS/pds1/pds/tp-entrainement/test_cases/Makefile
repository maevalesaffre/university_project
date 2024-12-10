CC=gcc
CFLAGS=-Wall -Wextra -Wno-unused-parameter -I ./pds_testlib
LDFLAGS=-fsanitize=thread -L ./pds_testlib
LIBS=-pthread -lpdstest

SRCS=$(wildcard *.c)
OBJS=$(SRCS:.c=.o)

TEST_SRCS=$(wildcard *.c)
TEST_SRCS := $(filter-out common_tests.c, $(TEST_SRCS))
TEST_OBJS=$(TEST_SRCS:.c=.o)
TEST_EXES=$(TEST_SRCS:.c=)

.PRECIOUS: %.o

.PHONY: all clean test test-docker

all : $(TEST_EXES)

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

test1: test1.o ../ex1/answers.o
	$(CC) $(LDFLAGS) -o $@ $^ $(LIBS) 

test2: test2.o ../ex1/answers.o 
	$(CC) $(LDFLAGS) -o $@ $^ $(LIBS) 

test3: test3.o ../ex1/answers.o
	$(CC) $(LDFLAGS) -o $@ $^ $(LIBS) 

test4: test4.o ../ex1/answers.o 
	$(CC) $(LDFLAGS) -o $@ $^ $(LIBS) 

test5: test5.o ../ex1/answers.o
	$(CC) $(LDFLAGS) -o $@ $^ $(LIBS) 

test6: test6.o ../ex1/answers.o 
	$(CC) $(LDFLAGS) -o $@ $^ $(LIBS) 

test_ex2: test_ex2.o ../ex2/answers.o 
	$(CC) $(LDFLAGS) -o $@ $^ $(LIBS) 

clean:
	rm -f $(OBJS) $(EXE) $(TEST_OBJS) $(TEST_EXES)
	rm -f *~
	rm -f grade.txt

test: ${TEST_EXES}
	./run_tests.sh $(TEST_EXES)

test-docker:
	docker build -q -t eval_pds_docker .
	docker run --rm eval_pds_docker test


