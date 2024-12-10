CC = gcc
run : DNSsimple DNSsimple.c
	./DNSsimple

dns:
	make DNS;


DNSsimple : DNSsimple.c
	$(CC) $? -o $@

: %.c
	$(CC) $? -o $@

clean:
	rm -f $ DNSsimple DNS
