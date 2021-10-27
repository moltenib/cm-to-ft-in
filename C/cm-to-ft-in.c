#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    if (argc != 2) {
        printf("Usage: %s CM\n", argv[0]);
        return 1;
    }

    double cm = atof(argv[1]);

    int feet = trunc(cm / 30.48);
    double inches = trunc(fmod(cm, 30.48) / 0.254) / 10;

    printf("%d'%1g\"\n", feet, inches);
}
