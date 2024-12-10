CC      = gcc
CFLAGS  = -g -Wall -Wextra -fsanitize=address
LDFLAGS = -fsanitize=address

.PHONY: all clean realclean test test-docker

EXES   := on do args 

all : $(EXES)

on : on.c
	${CC} ${CFLAGS} $< -o $@ ${LDFLAGS}

do : do.o makeargv.o
	${CC} ${CFLAGS} $^ -o $@ ${LDFLAGS}

args : args.o makeargv.o
	${CC} ${CFLAGS} $^ -o $@ ${LDFLAGS}


.o:.c
	${CC} ${CFLAGS} -c $<


clean:
	rm -f core *.o

realclean: clean
	rm -rf ${EXES} *~ test_cases/__pycache__ test_cases/*~

test :
	test_cases/run_tests.sh

test-docker: 
	docker build -q -t eval_pds_docker .
	docker run --rm eval_pds_docker all test
