/*
 * =====================================================================================
 *
 *       Filename:  DNS.c
 *
 *    Description:
 *              - prend un lien url en argument
 *              - interroge un serveur dsn par rapport au nom de domaine.
 *
 *        Version:  1.0
 *        Created:  02/22/2022 02:53:13 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  DIAWARA Aboubacar (mn), aboubacar.diawara.etu@univ-lille.fr
 *        Company:
 *
 * =====================================================================================
 */
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
#define QR_HEADER_LEN 12
#define QR_ADDIT_LEN 5
#define DESTPORT 53
#define NS_ANSWER_MAXLEN 512
#define DESTIPV4 "127.0.0.53"

/**
 * @brief rempli l'en tête du MESSAGE.
 *
 * @param query
 */
void fill_header(unsigned char* query)
{
    unsigned char base[QR_HEADER_LEN] = {
        0x08,  0xbb,  0x01,  0x00,
        0x00,  0x01,  0x00,  0x00,
        0x00,  0x00,  0x00,  0x00,
    };

    /*
        /!\ameliorer, les 2 premiers octets sont aléatoires.
    */
    for (size_t i = 0; i < QR_HEADER_LEN; i++)
    {
        query[i] = base[i];
    }
}

/**
 * @brief remplie les informations additionnelles du MESSAGE.
 *
 * @param query
 * @param from position de depart de l'ecriture dans le tableau.
 */
void fill_others(unsigned char* query, size_t query_len)
{
    query[query_len-5] = 0x00;
    query[query_len-4] = 0x00;
    query[query_len-3] = 0x01;
    query[query_len-2] = 0x00;
    query[query_len-1] = 0x01;
}

/**
 * @brief retourne la taille de la ième sous domaine.
 * @example
 *      - size_i_subdomain("www.google.fr", 1) -> 3
 *      - size_i_subdomain("www.google.fr", 2) -> 6
 *      - size_i_subdomain("www.google.fr", 1) -> 2
 *
 * @param i
 * @return int
 */
int size_i_subdomain(char const *hostname, size_t i)
{
    size_t len = 0;
    size_t iem_domain = 1;
    unsigned char const *sub_domain = hostname;

    assert(i > 0 && i <= 3);
    // on se place sur le sous domaine visé
    while (iem_domain != i)
    {
        if (sub_domain[0] == '.')
        {
            iem_domain++;
        }
        sub_domain++;
    }

    // On ne peut avoir que 3 sous domaines au plus.
    assert(iem_domain < 4);

    // une fois sur le sous domaine, on calcul sa taille.
    while ( (sub_domain[0] != '.') && *sub_domain)
    {
        sub_domain++;
        len++;
    }

    return len;
}

/**
 * @brief insere le nom de domaine.
 *
 * @param hostname le nom de domaine
 * @param query le MESSAGE à completer.
 * CU: exactement 3 sous domaines dans la chaine.
 */
void fill_qname(char const* hostname, unsigned char* query)
{
    unsigned char const *c = hostname; /* www (3). dldsklds.. ()n . fr(2) */
    // on parcourt tout la chaine.
    size_t i_subdomain = 1;
    size_t i;
    query[QR_HEADER_LEN] = size_i_subdomain(hostname, i_subdomain);

    for (i = QR_HEADER_LEN+1; *c; i++)
    {
        // si c'est pas un point, inserer simplement le caractère
        if ('.' != *c)
        {
            query[i] = *c;
        }
        else {
            // si on rencontre un point alors:
                // c'est la fin d'un sous domaine
                // on inseère donc la taille du suivant. :)
            query[i] = size_i_subdomain(hostname, ++i_subdomain);
        }
        c++;
    }
    // après ecriture du nom de domaine,
    // on insère un zero terminator.
    query[i] = 0x00;
}

/**
 * @brief prepare the message which will be send to the DSN server.
 *
 * @param dest_name the distant host name.
 */
void prepare_message(char const *dest_name, unsigned char* query, size_t query_len)
{
    // remplir l'en-tête
    fill_header(query);
    // inserer le hostname.
    fill_qname(dest_name, query);
    // remplir les informations additionnelles
    fill_others(query, query_len);
}


/** Initialize the struct sockaddr with the giving information.
 * \param af_hints the struct to fill.
 */
int prepare_remote_addr(struct sockaddr_in *remote_addr)
{
    memset(remote_addr, 0, sizeof(struct sockaddr_in));
    remote_addr->sin_family      = AF_INET; /* IPv4 */
    remote_addr->sin_port        = htons(DESTPORT); /* numero de port dest */
    remote_addr->sin_addr.s_addr = inet_addr(DESTIPV4); /* @IPv4 dest */
    fprintf(stderr, " conversion de l'@IPv4, pour la chaine \"%s\" ... ", DESTIPV4);
    if (remote_addr->sin_addr.s_addr == INADDR_NONE) {
      fprintf(stderr,"[erreur] - inet_addr(\"%s\") -> Mauvais formatage\n", DESTIPV4);
      return EXIT_FAILURE;
    }
    fprintf(stderr, "[ok]\n");
    return EXIT_SUCCESS;
}

/**
 * @brief prepare the socket.
 *
 * @param af_result
 * @return int the socket descriptor.
 */
int prepare_socket()
{
    int sock = 0;
    fprintf(stderr, " creation du socket en mode DGRAM (UDP) ... ");
    sock = socket(PF_INET, SOCK_DGRAM, 0);
    if (sock < 0) {
      perror("[erreur] - socket ");
      return EXIT_FAILURE;
    }
    fprintf(stderr, "[ok]\n");

    return sock;
}

ssize_t reception_answ(int sock, char* answer)
{
    struct sockaddr_in addrRemoteFromRecv;
    socklen_t addrRemoteFromRecvlen = sizeof(struct sockaddr_in);
    ssize_t len;
    if ( (len = recvfrom(sock, answer, NS_ANSWER_MAXLEN, 0, (struct sockaddr *) &addrRemoteFromRecv, &addrRemoteFromRecvlen)) < 0) {
      perror("[erreur] - recvfrom ");
    }
    fprintf(stderr, "[ok]\n longueur du message recu : %ld\n", len);
    fprintf(stderr," - port  distant  : %hu\n", ntohs(addrRemoteFromRecv.sin_port));
    fprintf(stderr," - @IPv4 distante : %s\n", inet_ntoa(addrRemoteFromRecv.sin_addr));

    return len;
}

void display_answ(char *answer, size_t len)
{
    for (int i = 0; i < len; i++) {

      fprintf(stdout," %.2X", answer[i] & 0xff);

      if (((i+1)%16 == 0) || (i+1 == len)) {

        /* ceci pour afficher les caracteres ascii apres l'hexa */
        /* >>> */
        for (int j = i+1 ; j < ((i+16) & ~15); j++) {
          fprintf(stdout,"   ");
        }
        fprintf(stdout,"\t");
        for (int j = i & ~15; j <= i; j++)
          fprintf(stdout,"%c",answer[j] > 31 && answer[j] < 128 ? (char)answer[j] : '.');
        /* <<< */
        fprintf(stdout,"\n");
      }
    }
}

unsigned char * process_one_answer(unsigned char *answer_i)
{
    char *c  = answer_i + 12;
    // display the ip address.
    if (answer_i[3] == 1){
        printf("+ IPV4: ", c-1);
        int i = 1;
        while (i <= 4)
        {
            int n = (int) *c;
            if (n < 0) n += 256;
            printf("%d", n);
            if (i != 4) printf(".");
            i++;
            c++;
        }
        printf("\n");
        return c+4;
    } else {
        printf("+ CNAME: ");
        int i = 1;
        while (i <= 4)
        {
            int n = (int) *c;
            if (n < 0) n += 256;
            printf("%c", n);
            i++;
            c++;
        }
        printf("\n");
        return c;
    }
}

void process_answer(char *answer, size_t answer_len, size_t query_len)
{
    int answer_to_read = *(answer + 7); // nombre de reponses
    int current_answer = 1;
    unsigned char *current_response = answer + query_len;

    printf("nombre de reponses: %d \n", answer_to_read);

    while (current_answer <= answer_to_read)
    {
        // on determine le debut de la reponse
		// on se positionne sur l'indicateur d'une adresse
        while (*current_response != 0xc0) {
            printf("%d", *current_response);
            current_response++;
        }

        // on affiche la reponse.
        printf("+ reponse: %d\n", current_answer++);
        if (current_answer-1 != 1) current_response = current_response+2;
        current_response = process_one_answer(current_response);
    }
}


/**
 * @brief envoie le message au serveur DSN.
 *
 * @param querry
 */
void send_request(unsigned char* query, size_t query_len, char const* hostname)
{
    struct sockaddr_in remote_addr;
    int socket;
    ssize_t len;
    char buff[NS_ANSWER_MAXLEN];

    // [1] obtenir l'adresse ip  de la machine distante (serveur DSN à interroger)
    assert(prepare_remote_addr(&remote_addr) == EXIT_SUCCESS);

    // [2] creer le socket
    socket = prepare_socket();

    // [3] envoie du message
    len = sendto(
        socket,
        query,
        query_len,
        0,
        (struct sockaddr*) &remote_addr,
        sizeof(struct sockaddr_in)
    );

    if (len < 0) perror("[erreur] - sendto ");
    fprintf(stderr, "[ok]\n longueur du message envoye : %lu\n", len);

    // [4] reception reponse.
    ssize_t answer_len;
    answer_len = reception_answ(socket, buff);
    display_answ(buff, answer_len);

    // [5] analyse du message.
    process_answer(buff, answer_len, query_len);

    close(socket);
}

/**
 * argv[1] -> hostname
 */
int main(int argc, char const *argv[])
{
    assert(argc == 2); // usage de la commande

    char const *hostname = argv[1];
    size_t hostname_len = strlen(hostname) + 1;

    size_t query_len = QR_HEADER_LEN + hostname_len + QR_ADDIT_LEN;

    unsigned char* query = (unsigned char*) malloc(query_len*sizeof(unsigned char));

    prepare_message(hostname, query, query_len);
    send_request(query, query_len, hostname);

    // liberer la memoire
    free(query);

    return 0;
}
