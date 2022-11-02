#include <stdio.h>
#include <unistd.h>

void greet() {
  printf("Welcome to the Phonebook\n");
  printf("--------------------------\n");
  sleep(1);

  printf("The following commands are available:\n");
  sleep(1);
  printf("print\n");
  sleep(1);
  printf("store\n");
  sleep(1);
  printf("search\n");
  sleep(1);
  printf("remove\n");
  sleep(1);
}
