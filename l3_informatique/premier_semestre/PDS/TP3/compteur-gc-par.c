#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <assert.h>
#include <pthread.h>

typedef struct{
    long taille;
    char *th_bloc;
}th_arg;

unsigned long compteur_gc(char *bloc, unsigned long taille) {
    unsigned long i, cptr = 0;

    for (i = 0; i < taille; i++)
        if (bloc[i] == 'G' || bloc[i] == 'C')
            cptr++;

    return cptr;
}

void *compteur_gc_th(void *arg){
    th_arg *targ = (th_arg*) arg;
    long res = compteur_gc(targ->th_bloc, targ-> taille);
    return (void *)res;
}

int main(int argc, char *argv[]) {
    struct stat st;
    int fd;
    char *tampon;
    int lus;
    unsigned long cptr = 0;
    off_t taille = 0;
    struct timespec debut, fin;
    struct timespec debut_th, fin_th;

    assert(argc > 1);
    assert(argc == 3);

    /* Quelle taille ? */
    assert(stat(argv[2], &st) != -1);
    tampon = malloc(st.st_size);
    assert(tampon != NULL);

    /* Chargement en mémoire */
    fd = open(argv[2], O_RDONLY);
    assert(fd != -1);
    while ((lus = read(fd, tampon + taille, st.st_size - taille)) > 0)
        taille += lus;
    assert(lus != -1);
    assert(taille == st.st_size);
    close(fd);

    /* Nombres threads */
    assert(argc>0);
    pthread_t *threads;
    long num_threads;    
    int i;
    int rc;
    long res_total=0;
    num_threads=strtol(argv[1],NULL,10);
    th_arg *targ[num_threads];    
    threads=malloc(num_threads*sizeof(pthread_t));

    if(threads==NULL){
        perror("malloc");
        exit(EXIT_FAILURE);
    }

    
    assert(clock_gettime(CLOCK_MONOTONIC, &debut_th) != -1);
    for(i=0; i<num_threads;i++){
        targ[i]=malloc(num_threads*sizeof(th_arg));
        targ[i]->taille = taille/num_threads;
        targ[i]->th_bloc = tampon+i*targ[i]->taille;
        rc = pthread_create(&threads[i],NULL, compteur_gc_th,targ[i]);
        if(rc){
            printf("ERREUR code de retour pthread_create");
            exit(EXIT_FAILURE);
        }
    }

    for(i=0; i<num_threads;i++){
        long res;
        rc = pthread_join(threads[i],(void**)&res);
        if(rc){
            printf("ERREUR code de retour pthread_create");
            exit(EXIT_FAILURE);
        }
        res_total+=res;
    }
    assert(clock_gettime(CLOCK_MONOTONIC, &fin_th) != -1);


    /* Calcul proprement dit */
    assert(clock_gettime(CLOCK_MONOTONIC, &debut) != -1);
    cptr = compteur_gc(tampon, taille);    
    assert(clock_gettime(CLOCK_MONOTONIC, &fin) != -1);

    /* Affichage des résultats */
    printf("Nombres de GC:   %ld\n", cptr);
    printf("Taux de GC:      %lf\n", ((double) cptr) / ((double) taille));
    

    fin.tv_sec  -= debut.tv_sec;
    fin.tv_nsec -= debut.tv_nsec;
    if (fin.tv_nsec < 0) {
        fin.tv_sec--;
        fin.tv_nsec += 1000000000;
    }
    printf("Durée de calcul: %ld.%09ld\n", fin.tv_sec, fin.tv_nsec);
    printf("(Attention: très peu de chiffres après la virgule sont réellement significatifs !)\n\n\n");


    printf("Nombres de GC Thread:   %ld\n", res_total);
    printf("Taux de GC Thread:      %lf\n", ((double) res_total) / ((double) taille));

    fin_th.tv_sec  -= debut_th.tv_sec;
    fin_th.tv_nsec -= debut_th.tv_nsec;
    if (fin_th.tv_nsec < 0) {
        fin_th.tv_sec--;
        fin_th.tv_nsec += 1000000000;
    }
    printf("Durée de calcul: %ld.%09ld\n", fin_th.tv_sec, fin_th.tv_nsec);
    printf("(Attention: très peu de chiffres après la virgule sont réellement significatifs !)\n");

    free(tampon);
    
    return 0;
}