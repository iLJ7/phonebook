#include <stdio.h>
#include <unistd.h>
#include "binaryTree.c"  // Including our binaryTree.c file, which handles the operations to be carried out on the binary tree phonebook.

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

// Our setup insert function.
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

    insertBT(root, name, address, number);  // Calling our recursive insert function from binaryTrees.c
}

// Our setup remove function.
void removeUtil(struct node *root){

    char name[100];

    printf("Enter name to remove:\n");
    scanf("%s", name);

    removeBT(root, name);
}

// Our setup search function.
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
        searchBTname(root, name);  // Calling the recursive search-by-name function in binaryTrees.c
    }

    else if(option == 2){

        printf("Enter number to search for:\n");
        scanf("%d", &number);
        searchBTnumber(root, number);  // Calling the recursive search-by-number function in binaryTrees.c
    }

}
