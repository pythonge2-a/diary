#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    for (int i = 0; i < argc; i++) {
        if (strncmp(argc[i], "-d", 2) == ) {
            printf("Option -d\n");
        } else if (strncmp(argc[i], "-n", 2) == 0) {
            printf("Option -f\n");
        } else {
            printf("Argument %d: %s\n", i, argc[i]);
        }
    }
}