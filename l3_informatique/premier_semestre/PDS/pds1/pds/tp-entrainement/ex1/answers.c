#include "answers.h"

#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <semaphore.h>
#include <string.h>
#include <limits.h>

/* Exercice 1 */
void liste_sous_reps(char* dirname)
{
    struct stat s;
    char p[PATH_MAX];
    
    stat(dirname, &s);
    if (S_ISDIR(s.st_mode)) {
        DIR *dirp = opendir(dirname);
        struct dirent *dent;
        while ((dent = readdir(dirp))) {
            if ((strcmp(dent->d_name, ".") != 0) && 
                (strcmp(dent->d_name, "..") != 0)) {
            
                snprintf(p, PATH_MAX-1, "%s/%s", dirname, dent->d_name);
                stat(p, &s);
                if (S_ISDIR(s.st_mode)) 
                    affiche_str(p);
            }
        }
        closedir(dirp);
    }
}

