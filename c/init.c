#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    FILE *fp = fopen("init_write.txt", "w");
    fputs("Text sent from init.c, sort of...\n", fp);
    fputs("After running `gcc init.c` and `./a.out`", fp);
    fclose(fp);
    return 1;
}