#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main(void)
{
	char *s;
	unsigned long int i;

	buf = strdup("Need-to-change!");
	if (buf == NULL) {
		fprintf(stderr, "Can't allocate mem with malloc\n");
		return (EXIT_FAILURE);
	}

	i = 0;
	
	while (buf) {
		printf("[%lu] %s (%p)\n", i++, s, (void *)s);
		sleep(1);
	}
	return (EXIT_SUCCESS);
}
