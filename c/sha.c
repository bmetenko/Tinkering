#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <file1> <file2> ... <fileN>\n", argv[0]);
        return 1;
    }

    for (int i = 1; i < argc; i++) {
        const char *filename = argv[i];
        char command[1024]; // Assuming a reasonably large buffer for the command

        // Construct the command to calculate the SHA-256 hash
        snprintf(command, sizeof(command), "shasum -a 256 %s", filename);

        FILE* file = popen(command, "r"); // Open for reading
        if (file == NULL) {
            perror("popen");
            return 1;
        }

        char buffer[65]; // +1 for the null terminator

        if (fscanf(file, "%64s", buffer) == 1) {
            printf("SHA-256 of %s: %s\n", filename, buffer);
        } else {
            fprintf(stderr, "Error reading SHA-256 hash for %s.\n", filename);
        }

        pclose(file);
    }

    return 0;
}
