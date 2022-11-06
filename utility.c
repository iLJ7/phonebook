#include <stdio.h>
#include <unistd.h>
#include "binaryTree.c"

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

void insert(struct node *root) {

    char name[100];
    char address[100];
    int number;

    printf("Enter name to insert:\n");
    scanf("%s", name);

    printf("Enter address to insert:\n");
    scanf("%s", address);

    printf("Enter number to insert:\n");
    scanf("%d", &number);

    printf("%s %s %d\n", name, address, number);

    insertBT(root, name, address, number);
    /* call binaryTree insert function here. */
}

void removeUtil(struct node *root){

    char name[100];

    printf("Enter name to remove:\n");
    scanf("%s", name);

    removeBT(root, name);
}

void search(struct node *root){

    char name[100];
    int number;
    int option;

    printf("Enter:\n");
    printf("1 to search by name\n");
    printf("2 to search by number\n");

    scanf("%d", &option);

    if(option == 1){
        printf("Enter name to search for:\n");

        scanf("%s", name);
        searchBTname(root, name);
    }

    else if(option == 2){

        printf("Enter number to search for:\n");
        scanf("%d", &number);
        searchBTnumber(root, number);
    }

}
