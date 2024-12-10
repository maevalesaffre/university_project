#######################################
### THIS FILE SHOULD NOT BE CHANGED ###
#######################################

CC=gcc
CFLAGS=-Wall -Wextra -Wno-unused-parameter
LDFLAGS=-pthread -fsanitize=address

EXE=prg
SRCS=$(wildcard *.c)
OBJS=$(SRCS:.c=.o)

.PRECIOUS: %.o

.PHONY: clean test test-docker

$(EXE): $(OBJS)
	$(CC) $(LDFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	rm -f $(OBJS) $(EXE) $(TEST_OBJS) $(TEST_EXES) test_cases/common_tests.o
	rm -f *~

