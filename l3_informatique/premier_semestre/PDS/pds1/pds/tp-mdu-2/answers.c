#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <assert.h>
#include <dirent.h>
#include <string.h>
#include <limits.h>
#include <search.h>

/* Definition des variables globales */
int opt_follow_links = 0;
int opt_apparent_size = 0;

#define MAX_FILES 1024

static char *all_keys[MAX_FILES];
static int last_key = 0;

int has_been_visited(struct stat *s)
{
    ENTRY elem;
    elem.key = (char *)malloc(16);
    elem.data = NULL;
    sprintf(elem.key, "%lu", s->st_ino);
    if (hsearch(elem, FIND) == NULL) {
        hsearch(elem, ENTER);
        all_keys[last_key++] = elem.key;
        return 0;
    }
    else {
        free(elem.key);
        return 1;
    }
}

int mystat(const char *pathname, struct stat *s)
{
    if (opt_follow_links) return stat(pathname, s);
    return lstat(pathname, s);
}

int get_size(struct stat *s)
{
    if (opt_apparent_size) {
        return s->st_size;
    }
    else return s->st_blocks;
}


/* Exercice 1 */
int du_single_file_intern(const char *pathname);

int du_single_file(const char *pathname) {
  hcreate(MAX_FILES);
  int res = du_single_file_intern(pathname);
  // free all memory
  hdestroy();
  for (int i=0; i<last_key; i++) free(all_keys[i]);
  last_key = 0;
  
  return res;
}
int du_single_file_intern(const char *pathname)
{
    struct stat s;

    int ret = mystat(pathname, &s);
    if (ret != 0) {
        perror("Cannot open file");
        return -1;
    }
    if ( has_been_visited(&s) ) return 0;
    else return get_size(&s);
}


/* Exercice 2 */
int is_dir(const char * pathname)
{
    struct stat s;

    int ret = mystat(pathname, &s);
    if (ret != 0) {
        perror("Cannot open file");
        return -1;
    }
    if (S_ISDIR(s.st_mode)) return 1;
    else return 0;
}


/* Exercice 3 */
int du_file_intern(const char *pathname);
int du_file(const char *pathname) {
  hcreate(1024);
  int res = du_file_intern(pathname);
  hdestroy();
  return res;
}

int du_file_intern(const char *pathname)
{
    int size = du_single_file_intern(pathname);
    if (size <= 0)
        return 0;
    
    if (is_dir(pathname) == 1) {
        DIR *dirp = opendir(pathname);
        struct dirent *d = readdir(dirp);
        while (d != NULL) {
            if ((strcmp(".", d->d_name) != 0) && (strcmp("..", d->d_name) != 0)) {
                char name[PATH_MAX];
                sprintf(name, "%s/%s",pathname, d->d_name); 
                size += du_file_intern(name);
            } 
            d = readdir(dirp);
        }
        closedir(dirp);
    }
    return size;
}
