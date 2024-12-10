CC      = gcc
CFLAGS  = -Wall -Wextra -fsanitize=thread
CFLAGS += -g
LDFLAGS = -pthread -fsanitize=thread

libpdstest.a : testlib.o tlogger.o
	ar -crs libpdstest.a testlib.o tlogger.o

test_lib.o : test_lib.c test_lib.h
	$(CC) -c $(CFLAGS) $<

tlogger.o : tlogger.c tlogger.h testlib.h
	$(CC) -c $(CFLAGS) $< 


clean :
	rm -f *.o
	rm -f *~
