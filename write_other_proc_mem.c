#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char **argv) {
    char filename[64], buf[20];
    int offset, fd;

    if (argc != 4) {
        printf("Usage: %s <pid> <offset> <string-to-write>", argv[0]);
        exit(EXIT_FAILURE);
    }

    sprintf(filename, "/proc/%s/mem", argv[1]);
    printf("Write into %s", filename);

    if ((fd = open(filename, O_WRONLY)) < 0) {
        perror("open");
        exit(EXIT_FAILURE);
    }

    offset = strtol(argv[2], 0, 16);

    if ((pwrite(fd, argv[3], 100, offset)) < 0) {
        perror("pwrite");
        exit(EXIT_FAILURE);
    }

    close(fd);
    
    return 0;
}
