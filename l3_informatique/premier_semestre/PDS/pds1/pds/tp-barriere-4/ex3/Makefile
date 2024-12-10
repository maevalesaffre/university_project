CC      = gcc
CFLAGS  = -Wall -Wextra -fsanitize=thread
CFLAGS += -g
LDFLAGS = -pthread -fsanitize=thread

TOUS := prodcons

all : $(TOUS)

.o:.c
	${CC} ${CFLAGS} $<

prodcons : answers.o prodcons.o 
	${CC} ${LDFLAGS} $^ -o $@

clean :
	rm -rf *.o
	rm -rf $(TOUS)
	rm -rf *~


