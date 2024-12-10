#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include "answers.h"

int main(int argc, char *argv[])
{
    int opt;

    while ((opt = getopt(argc, argv, "bL")) != -1) {
        switch(opt) {
        case 'b' : opt_apparent_size = 1;
            break;
        case 'L' : opt_follow_links = 1;
            break;
        default :
            printf("Unknown option\n");
            printf("Usage: %s [-b] [-L] filename\n", argv[0]);
            exit(EXIT_FAILURE);
        }
    }
    if (optind >= argc) {
        printf("Expecting argument\n");
        printf("Usage: %s [-b] [-L] filename\n", argv[0]);
            exit(EXIT_FAILURE);
    }
    
    int s = du_file(argv[optind]);
    printf("%d\t%s\n", s, argv[optind]);

    return EXIT_SUCCESS;
}
