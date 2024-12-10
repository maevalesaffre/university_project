CC      = gcc
CFLAGS  = -Wall -fsanitize=thread -Wno-unused-parameters
CFLAGS += -g
LDFLAGS = -pthread -fsanitize=thread

TESTS = test_ex1 test_ex2 test_ex3 
LIB_OBJS = logger.o common_tests.o

all : ${TESTS} run

.o:.c
	${CC} ${CFLAGS} $<

test_ex1 : test_ex1.o ../ex1/answers.o ${LIB_OBJS}
	${CC} ${LDFLAGS} $^ -o $@

test_ex2 : test_ex2.o ../ex2/answers.o ${LIB_OBJS}
	${CC} ${LDFLAGS} $^ -o $@

test_ex3 : test_ex3.o ../ex3/answers.o ${LIB_OBJS}
	${CC} ${LDFLAGS} $^ -o $@

run :
	./test_ex1
	./test_ex2
	./test_ex3


clean :
	rm -f *.o
	rm -f ${TESTS} 	
	rm -f *~
