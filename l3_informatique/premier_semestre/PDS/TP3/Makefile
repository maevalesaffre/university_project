ERROR = -Wall -Werror -Wextra

all:
	make compteur-gc-par;make aleazard;make compteur-gc;./aleazard 10000000 > genome.txt
compteur-gc-par: compteur-gc-par.o 
	gcc -o $@ $^
aleazard: aleazard.o 
	gcc -o $@ $^
compteur-gc: compteur-gc.o 
	gcc -o $@ $^
%.o: %.c
	gcc $(ERROR) -c $^
clean:
	rm -f *.o;rm aleazard;rm compteur-gc;rm compteur-gc-par;rm genome.txt