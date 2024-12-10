#include <stdio.h>
#include <fcntl.h>
#include <dirent.h>
#include <stdlib.h>


void mls(char *name) {
  DIR *d;
  struct dirent *ent;

  d=opendir(name);
  if(d==NULL) {
    fprintf(stderr,"Warning : unable to open %s\n",name);
    exit(EXIT_FAILURE);
  }

  while((ent=readdir(d)) != NULL) {
    printf("%s\n", ent->d_name);
  }

  closedir(d);

}


int main(int argc, char **argv)
{
  char *root_name;

  if(argc==2) {
    /* affichage en blocs */
    root_name=argv[1];
  } else {
    fprintf(stderr,"Usage : mls dir_name\n");
    exit(EXIT_FAILURE);
  }

  mls(root_name);

  return EXIT_SUCCESS;

}
