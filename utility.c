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

    printf("Enter name:\n");
    scanf("%s", name);

    printf("Enter address:\n");
    scanf("%s", address);

    printf("Enter number:\n");
    scanf("%d", &number);

    printf("%s %s %d\n", name, address, number);

    /* call binaryTree insert function here. */
    if(root->left){
        insert(root->left);
    }

    else if(root->right){
        insert(root->right);
    }

    else{
        root->left = createNode(name, address, number);
    }
}
