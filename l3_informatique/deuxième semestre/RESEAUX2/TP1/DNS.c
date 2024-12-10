#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include <netdb.h>
#include <unistd.h>
#include <assert.h>

#define LEN_HEADER 12
#define LEN_ADDIT 5
#define DESTINATION_PORT 53
#define ANSWER_MAXLEN 512
#define DESTINATION_IPV4 "127.0.0.53"

/**
 * ajoute l'entete du message.
 *
 * @param query
 */
void fill_header(unsigned char* query){
    unsigned char base[LEN_HEADER] = { // creer un tableau de taille 12 qu'on nomme base (taille de l'en-tete) et les 12 premiers elts de query vont etre les 12 premiers elts de query
        0x08,  0xbb,  0x01,  0x00,
        0x00,  0x01,  0x00,  0x00,
        0x00,  0x00,  0x00,  0x00,
    };    
    for (size_t i = 0; i < LEN_HEADER; i++){
        query[i] = base[i];
    }
}

/**
 * ajoute les informations additionnelles du message.
 *
 * @param query le message a completer.
 * @param query_len taille message.
 */
void fill_residus(unsigned char* query, size_t query_len){
    query[query_len-5] = 0x00;
    query[query_len-4] = 0x00;
    query[query_len-3] = 0x01;
    query[query_len-2] = 0x00;
    query[query_len-1] = 0x01;
}

/**
 * retourne la taille du ieme sous domaine.
 * @param hostname le nom de domaine
 * @param i
 */
int size_i_subdomain(char const *hostname, size_t i){
    size_t len = 0; // on instancie la taille du domaine a 0
    size_t iem_domain = 1; // on instancie la taille du iem sous domain a 1
    unsigned char const *sub_domain = hostname; // sub_domain va pointer vers la variable hostname
    assert(i > 0);
    // on se place sur le sous domaine voulu en checkant si le premier elt est un point
    while (iem_domain != i){
        if (sub_domain[0] == '.'){
            iem_domain++;
        }
        sub_domain++;
    }
    // une fois sur le sous domaine, on calcule sa taille.
    while ( (sub_domain[0] != '.') && *sub_domain){
        sub_domain++;
        len++;
    }
    return len;
}

/**
 * rajoute le nom de domaine.
 * @param hostname le nom de domaine
 * @param query le message a completer.
 */
void fill_name(char const* hostname, unsigned char* query){
    unsigned char const *c = hostname; //c qui pointe sur hostname, le but est de parcourir toute la chaine
    size_t i_subdomain = 1;
    size_t i;
    query[LEN_HEADER] = size_i_subdomain(hostname, i_subdomain);
    for (i = LEN_HEADER+1; *c; i++){
        // si c'est pas un point, inserer simplement le caractere
        if ('.' != *c){
            query[i] = *c;
        }
        else {
            // si on rencontre un point alors, c'est la fin d'un sous domaine et on insere donc la taille du suivant. 
            query[i] = size_i_subdomain(hostname, ++i_subdomain);
        }
        c++;
    }
    // apres ecriture du nom de domaine, on insere un 0x00 (ou zero) a la ieme place pour fermer.
    query[i] = 0x00;
}

/**
 * prepare le message qui sera transmis au serveur DSN.
 * @param dest_name le nom de domaine distant
 * @param query le message a completer
 * @param query_len la taille dumessage a completer
 */
void prepare_message(char const *dest_name, unsigned char* query, size_t query_len){ //on fait l'en-tete, ensuite on insere le hostname et apres on termine par donner les infos add
    //l'en-tete
    fill_header(query);
    // inserer le hostname.
    fill_name(dest_name, query);
    // remplir les informations additionnelles
    fill_residus(query, query_len);
}


/** initialise la structure sockaddre avec les info 
 * @param fill_addr la structure a remplir
 */
int prepare_fill_addr(struct sockaddr_in *fill_addr){
    memset(fill_addr, 0, sizeof(struct sockaddr_in)); // memcet permet de remplir une zone memoire, identifiee par son adresse et sa taille, avec une valeur precise
    fill_addr->sin_family      = AF_INET; // IPv4 
    fill_addr->sin_port        = htons(DESTINATION_PORT); // numero de port dest 
    fill_addr->sin_addr.s_addr = inet_addr(DESTINATION_IPV4); // @IPv4 dest 
    fprintf(stderr, " conversion de l'@IPv4, pour la chaine \"%s\" ... ", DESTINATION_IPV4);
    if (fill_addr->sin_addr.s_addr == INADDR_NONE) {
      fprintf(stderr,"[erreur] - inet_addr(\"%s\") -> Mauvais formatage\n", DESTINATION_IPV4);
      return EXIT_FAILURE;
    }
    fprintf(stderr, "success\n");
    return EXIT_SUCCESS;
}

/**
 * prepare la socket et retourne la socket.
 */
int prepare_socket(){
    int sock = 0;
    fprintf(stderr, " creation de la socket ");
    sock = socket(PF_INET, SOCK_DGRAM, 0);
    if (sock < 0) {
      perror("fail, socket not create ");
      return EXIT_FAILURE;
    }
    fprintf(stderr, "success\n");
    return sock;
}

/** taille de la reponse
 * @param sock la socket
 * @param answer la reponse
 */
ssize_t reception_answ(int sock, char* answer){
    struct sockaddr_in addrRemoteFromRecv;
    socklen_t addrRemoteFromRecvlen = sizeof(struct sockaddr_in);
    ssize_t len;
    if ( (len = recvfrom(sock, answer, ANSWER_MAXLEN, 0, (struct sockaddr *) &addrRemoteFromRecv, &addrRemoteFromRecvlen)) < 0) {
      perror("[erreur] - recvfrom ");
    }
    fprintf(stderr, "[ok]\n longueur du message recu : %ld\n", len);
    fprintf(stderr," - port  distant  : %hu\n", ntohs(addrRemoteFromRecv.sin_port));
    fprintf(stderr," - @IPv4 distante : %s\n", inet_ntoa(addrRemoteFromRecv.sin_addr));
    return len;
}

/** affiche la reponse 
 * @param answer la reponse
 * @param len taille de la reponse
 */
void display_answ(char *answer, size_t len){
    for (int i = 0; i < len; i++) {
      fprintf(stdout," %.2X", answer[i] & 0xff);

      if (((i+1)%16 == 0) || (i+1 == len)) {

        /* pour afficher les caracteres ascii apres l'hexa */
        for (int j = i+1 ; j < ((i+16) & ~15); j++) {
          fprintf(stdout,"   ");
        }
        fprintf(stdout,"\t");
        for (int j = i & ~15; j <= i; j++)
          fprintf(stdout,"%c",answer[j] > 31 && answer[j] < 128 ? (char)answer[j] : '.');
        fprintf(stdout,"\n");
      }
    }
}

/** affiche le nom dans la reponse
 * @param name_position la position du prenom dans la reponse
 * @param complete_answer le reponse complete
*/
void display_name(int name_position, unsigned char *complete_answer){
	int first = 1;
	unsigned char  *c = complete_answer+name_position;
	while (*c) {
		if (*c > 0 && *c <= 9 && !first) printf(".");
		else printf("%c", *c);
		c++;
		first = 0;
	}
	printf("\n");
}


/** affiche l'IP dans la reponse recu
 * @param ip_adress l'addresse ip dans la reponse
*/
void display_adress(unsigned char *ip_adress){
	printf("- IPV4: ");
	for (size_t i = 0; i < 4; i++) {
		int n = ip_adress[i];
		if (n < 0) n += 256;
		printf("%d", n);
		if (i != 3){
            printf("."); // pas de point a la fin
        }
	}
	printf("\n");
}

/** affiche le cname
 * @param cname_adress le nom de l'addresse
*/
void display_cname(unsigned char *cname_adress)
{
	printf("- CNAME\n");
}

/** affiche le type
 * @param type le type
*/
void display_type(int type){
	printf("- TYPE: ");
	switch (type) {
		case 1:
			printf("adress");
			break;
		case 5:
			printf("canonique name");
			break;
		default:
			printf("(autres type non encore précisé)\n");
	}
	printf("\n");
}

/** 
 * @param answer_adress l'addresse de la reponse
 * @param complete_answer reponse complete
*/
unsigned char * process_one_answer(unsigned char *answer_adress, unsigned char *complete_answer){
	// verifier qu'on est bien sur un indicateur de pointeur
	assert(*answer_adress == 0xc0);
	int type = ((int) answer_adress[3]);
	int data_length = answer_adress[11];
	int answer_len = 12 + data_length;
	// afficher le nom
	printf("- NAME: ");
	display_name((int) answer_adress[1], complete_answer);
	// afficher le type
	display_type(type);
	if (type == 1){
     display_adress(answer_adress+12);
    }
	else if (type == 5){
        display_cname(answer_adress+12);
    }
	return answer_adress + answer_len;
}

/** 
 * @param answer la reponse
 * @param answer_len taille de la reponse
 * @param query_len taille du message
*/
void process_answer(char *answer, size_t answer_len, size_t query_len){
    int answer_to_read = *(answer + 7); 
    int current_answer = 1;
    unsigned char *current_response = answer + query_len; 
    printf("nombre de reponses: %d \n", answer_to_read);
    while (current_answer <= answer_to_read){
        // on determine le debut de la reponse
		// on se positionne sur l'indicateur d'une adresse
        while (*current_response != 0xc0){
            current_response++;
        }
        // on affiche la reponse.
		printf("+ reponse: %d\n", current_answer);
		current_response = process_one_answer(current_response, answer);
		// on passe a la reponse suivante
		current_answer++;
    }
}


/**
 * envoie le message au serveur DSN.
 * @param querry
 * @param query_len la longueur
 * @param hostname hostname
 */
void send_request(unsigned char* query, size_t query_len, char const* hostname){
    struct sockaddr_in fill_addr;
    int socket;
    ssize_t len;
    ssize_t answer_len;
    char buff[ANSWER_MAXLEN];  
    assert(prepare_fill_addr(&fill_addr) == EXIT_SUCCESS); // obtenir l'adresse ip  de la machine distante (serveur DSN a interroger)
    socket = prepare_socket(); // creer socket   
    len = sendto(socket,query,query_len,0,(struct sockaddr*) &fill_addr,sizeof(struct sockaddr_in)); //envoie du message
    if (len < 0){
        perror("[erreur] - sendto ");
    }
    fprintf(stderr, "[ok]\n longueur du message envoye : %lu\n", len);    
    answer_len = reception_answ(socket, buff); // reception reponse
    display_answ(buff, answer_len); //affichage message
    process_answer(buff, answer_len, query_len); //analyse du message
    close(socket);
}


int main(int argc, char const *argv[]){
    assert(argc == 2); // usage de la commande
    char const *hostname = argv[1];
    size_t hostname_len = strlen(hostname) + 1;
    size_t query_len = LEN_HEADER + hostname_len + LEN_ADDIT;
    unsigned char* query = (unsigned char*) malloc(query_len*sizeof(unsigned char));
    prepare_message(hostname, query, query_len);
    send_request(query, query_len, hostname);
    free(query);
    return 0;
}
