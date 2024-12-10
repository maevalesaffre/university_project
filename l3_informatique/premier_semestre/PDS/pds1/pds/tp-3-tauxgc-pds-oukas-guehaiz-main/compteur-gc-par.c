#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <assert.h>
/*rajouter */
#include <math.h>
#include <string.h>

/* struc pour le wrapper*/
struct param {
    char* chaine;
    int taille;
    unsigned long cptr;
};





unsigned long compteur_gc(char *bloc, unsigned long taille) {
    unsigned long i, cptr = 0;

    for (i = 0; i < taille; i++)
        if (bloc[i] == 'G' || bloc[i] == 'C')
            cptr++;

    return cptr;
}

void* compteur_gc_wrapper(void* arg){
    struct param *p = (struct param*) arg;
        p->cptr = compteur_gc(p->chaine, p->taille);
        return NULL;


} 

int main(int argc, char *argv[]) {
    assert(argc > 1);
    struct stat st;
    int fd;
    char *tampon;
    int lus;
    unsigned long cptr = 0;
    off_t taille = 0;
    struct timespec debut, fin;

    /* nombre de t threads (donc recherche)*/
    int n = (int) argv[2];
    int status;

    /* PARAMETRE DE NOS THREADS*/
    pthread_t tid[n];
    struct param param[n];

    

    /* Quelle taille ? */
    assert(stat(argv[1], &st) != -1);
    tampon = malloc(st.st_size);
    assert(tampon != NULL);

    /* Chargement en mémoire */
    fd = open(argv[1], O_RDONLY);
    assert(fd != -1);
    while ((lus = read(fd, tampon + taille, st.st_size - taille)) > 0)
        taille += lus;
    assert(lus != -1);
    assert(taille == st.st_size);
    close(fd);

    /* initialisation des parametres pour les threads */
    int taille_param=0,mod,i,j;
    /* initialisation d'un buffer provisoire*/
    char* buffer_tmp = malloc(st.st_size);
    assert(buffer_tmp != NULL);
    strcpy(buffer_tmp,tampon);

    for (i=0 ; i< n;i++){
        if(taille % n == 0){ 
            taille_param +=taille / n;
            param[i].taille = taille_param ;
        }

        else{
            
            taille_param += floor( taille / n);
            param[0].taille = taille_param+(taille %n);
            
            param[i].taille = taille_param;
        }
        
        for (j =0; j < param[i].taille ; j++){
            param[i].chaine[i]= buffer_tmp[j];
        }

        buffer_tmp += param[i].taille;
    }
    

    /* Calcul proprement dit */
    assert(clock_gettime(CLOCK_MONOTONIC, &debut) != -1);
    
    /* creation et execution des threads*/
    for (i=0 ; i< n;i++){
        status = pthread_create(&tid[i],NULL,compteur_gc_wrapper,(void*)param[i]); 
        assert(status == 0);
    }
    /* s'assurer que le threads se termine avant de recup la valeur de cptr*/
    for (i=0 ; i< n;i++){
        status = pthread_join(tid[i],NULL); 
        assert(status == 0);
        cptr += param[i].cptr;
    }

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
    printf("(Attention: très peu de chiffres après la virgule sont réellement significatifs !)\n");

    free(tampon);
    
    return 0;
}
