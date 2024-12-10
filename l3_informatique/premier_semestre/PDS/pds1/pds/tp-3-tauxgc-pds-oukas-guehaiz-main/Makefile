CC      = gcc
CFLAGS  = -Wall -Wextra -fsanitize=address -fno-omit-frame-pointer
CFLAGS += -g
LDFLAGS = -pthread -fsanitize=address

TOUS := aleazard compteur-gc compteur-gc-par

tout: ${TOUS}

aleazard: aleazard.c
	${CC} ${CFLAGS} $< -o $@ ${LDFLAGS}

compteur-gc: compteur-gc.c
	${CC} ${CFLAGS} $< -o $@ ${LDFLAGS}


compteur-gc-par: compteur-gc-par.c
	${CC} ${CFLAGS} $< -o $@ ${LDFLAGS}



clean:
	rm -f core *.o

realclean: clean
	rm -f ${TOUS}

.PHONY: all clean realclean
