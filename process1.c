#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main() {
  char fo[] = "I am Process-1";
  char* fo_addr = fo; // 
  int pid = getpid(); //

  printf("%s %p %d\n", fo, (void*)fo_addr, pid);

  printf("Now execute\n");
  printf("sudo ./proccess1 %d  %lx  %zu\n", pid, (long unsigned int) fo, strlen(fo)+1);

  printf("Press enter to start monitoring string fo, its address, and pid\n");
  getchar();

  while (1) {
    printf("%s %p %d\n", fo, (void*)fo_addr, pid);
    sleep(1);
  }

  return 0;
}
