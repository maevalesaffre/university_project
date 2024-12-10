#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <netdb.h>
#define MAXLINE 1024
#define PORT 5000

// reception UDP
int main() {
    int sock; // identifiant de socket
    struct sockaddr_in addrLocal; // struct pour Fixer (@IP,#Port) adresse Local
    struct sockaddr_in addrFrom; 
    char buffer[MAXLINE]; // la taille max du buffer
    if ( (sock = socket(AF_INET, SOCK_DGRAM, 0)) < 0 ) {
		perror("socket creation failed");
		exit(EXIT_FAILURE);
	}
    memset(&addrLocal, 0, sizeof(addrLocal)); // permet de remplir une zone mémoire, identifiée par son adresse et sa taille, avec une valeur précise.

    addrLocal.sin_family = AF_INET;
    addrLocal.sin_addr.s_addr = INADDR_ANY;
    addrLocal.sin_port = htons(PORT); //Port ouvert

    if ( bind(sock, (struct sockaddr *) &addrLocal, sizeof(addrLocal)) < 0 ){
        perror("bind failed");
        exit(EXIT_FAILURE);
    }

    socklen_t len = sizeof (struct sockaddr_in);
    if (recvfrom(sock, buffer, MAXLINE, 0 , (struct sockaddr*)&addrFrom, &len) <0){
        perror(" failed");
    }

    close(sock);
    printf("Client : %s\n", buffer);
}

