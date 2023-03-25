#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>

int main(int ac, char **av) {
    char filename[64], buf[20];
    int mem_addr;
    FILE *fp;
    
    setvbuf(stdin, 0, 0, 0);
    
    if (ac != 3) {
        fprintf(stderr, "usage: %s pid address\n", av[0]);
        exit(1); 
    }

    sprintf(filename, "/proc/%s/mem", av[1]);
    mem_addr = strtol(av[2], 0, 0);

    if ((fp = fopen(filename, "rw")) < 0) {
        fprintf(stderr, "Can't access pid %s", av[1]);
        exit(1);
    }
    printf("%x\n", mem_addr);
    fseek(fp, mem_addr, SEEK_SET);
    if (fwrite("hello, word!\x00", 13, 1, fp) < 0)
        perror("fwrite");
    else
        printf("Write OK\n");

    fseek(fp, mem_addr, SEEK_SET);
    if (fread(buf, 13, 1, fp) < 0)
        perror("fread");
    else {
        puts(buf);
        printf("Read OK\n");
    }
    
    return 0;
}
