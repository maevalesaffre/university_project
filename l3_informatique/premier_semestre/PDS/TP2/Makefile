ERROR = -Wall -Werror -Wextra

tests: main.o 
	gcc -o $@ $^
%.o: %.c
	gcc $(ERROR) -c $^
clean:
	rm -f *.o;rm tests