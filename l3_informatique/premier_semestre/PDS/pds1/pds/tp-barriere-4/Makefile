CC      = gcc
CFLAGS  = -Wall -Wextra -fsanitize=thread
CFLAGS += -g
LDFLAGS = -pthread -fsanitize=thread

all : 
	make -C ex1
	make -C ex2
	make -C ex3

test: 
	make -C test_cases

clean :
	make -C ex1 clean
	make -C ex2 clean
	make -C ex3 clean
	make -C test_cases clean
	rm -rf *~


