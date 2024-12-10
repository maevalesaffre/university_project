CC      = gcc
CFLAGS  = -Wall -Wextra -fsanitize=thread
CFLAGS += -g
LDFLAGS = -pthread -fsanitize=thread

TOUS := barr barr3 barr3-sol philosophes

all : $(TOUS)

barr : barr.c
	${CC} ${CFLAGS} $< -o $@ ${LDFLAGS}

barr3: barr3.c
	${CC} ${CFLAGS} $< -o $@ ${LDFLAGS}

barr3-sol: barr3-sol.c
	${CC} ${CFLAGS} $< -o $@ ${LDFLAGS}

philosophes : philosophes.c
	${CC} ${CFLAGS} $< -o $@ ${LDFLAGS}


clean :
	rm -rf *.o
	rm -rf $(TOUS)
	rm *~


