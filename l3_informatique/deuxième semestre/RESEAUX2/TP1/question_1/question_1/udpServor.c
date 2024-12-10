#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <netdb.h>

#define PORT 5000
#define MAXLINE 1024
	

// emission UDP
int main() {
	int sock; // identifiant de socket
	struct sockaddr_in addrDest; // struct pour Fixer (@IP,#Port) de destination
	struct hostent *hp; // struct pour Résolution Symbolique 
	const char *hello = "Hello from client"; //le message qu'on souahite envoyer
	
	if ( (sock = socket(AF_INET, SOCK_DGRAM, 0)) < 0 ) { //La famille d’adresses AF_INET est la famille d’adresses pour IPv4, SOCK_DGRAM Transmissions sans connexion, non garantie, de datagrammes de longueur maximale fixe.
		perror("socket creation failed");
		exit(EXIT_FAILURE);
	}

	// initialisation de l’(@IP,#Port) de destination 
	hp = gethostbyname("localhost"); // on récupère le hostname
	addrDest.sin_family = AF_INET;
    memcpy(&addrDest.sin_addr, hp->h_addr, hp->h_length);  // @IP de brigant.lifl.fr
	addrDest.sin_port = htons(PORT); //Port ouvert
	
	// memcpy permet de copier un bloc de mémoire spécifié par le paramètre source,
	// et dont la taille est spécifiée via le paramètre size, dans un nouvel emplacement
	// désigné par le paramètre destination. Il est bien entendu qu'il est de votre responsabilité 
	//d'allouer suffisamment de mémoire pour le bloc de destination afin qu'il puisse contenir toutes les données.
	
	
	sendto(sock, hello, strlen(hello), MSG_CONFIRM, (struct sockaddr*) &addrDest, sizeof(addrDest));
    printf("Hello message sent.\n");
	close(sock); //ferme la socket
	return 0;

	// MSG_CONFIRM Indiquer  à la couche liaison qu'une réponse correcte a été reçue du correspondant.
    // Si  la  couche  de  liaison  n'a  pas  cette  confirmation,  elle  va  réinterroger
    // régulièrement le voisinage. Seulement valide pour les sockets SOCK_DGRAM et SOCK_RAW et uniquement  implémenté  pour  IPv4  et  IPv6.
}


