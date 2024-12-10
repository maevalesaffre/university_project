CC      = gcc
CFLAGS  = -Wall -fsanitize=thread -Wno-unused-parameters
CFLAGS += -g
LDFLAGS = -pthread -fsanitize=thread

TOUS := barr 

all : $(TOUS)

.o:.c
	${CC} ${CFLAGS} $<

barr : answers.o barr.o 
	${CC} ${LDFLAGS} $^ -o $@

clean :
	rm -rf *.o
	rm -rf $(TOUS)
	rm -rf *~


