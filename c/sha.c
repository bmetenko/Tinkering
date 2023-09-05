#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main() {
    FILE* file = popen("shasum -a 256 init_write.txt", "r"); // Open for reading
    if (file == NULL) {
        perror("popen");
        return 1;
    }

    char buffer[65]; // +1 for the null terminator

    if (fscanf(file, "%64s", buffer) == 1) {
        printf("buffer is: %s\n", buffer);
    } else {
        fprintf(stderr, "Error reading SHA-256 hash.\n");
    }

    pclose(file);
    return 0;
}
