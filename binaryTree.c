#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Modelling our node with a struct.
struct node {
  char name[50];
  char address[50];
  int number;

  struct node* left;
  struct node* right;
};

// Creating our function declarations.
void printNode(struct node* root);
void searchBTname(struct node* root, char* name);
void searchBTnumber(struct node* root, int number);
const char* toLowercase(char* str);

// Our create node function. We allocate the correct amount of memory and store the name, address and number.
struct node* createNode(char* name, char* address, int number) {
  struct node* newNode = malloc(sizeof(struct node));
  strcpy(newNode->name, name);
  strcpy(newNode->address, address);
  newNode->number = number;

  newNode->left = NULL;
  newNode->right = NULL;

  return newNode;
}

// Our function to print the entire tree by in-order traversal.
void printTree(struct node *node)
{
    /*If tree has nodes:*/
    if (node != NULL) {
        if(node->left){
            printTree(node->left);
        }

        printNode(node);

        if(node->right){
            printTree(node->right);
        }
    }
}

// Our recursive function to insert a node into the tree.
void insertBT(struct node *node, char *name, char *address, int number){

  if(node->left){
    insertBT(node->left, name, address, number);
  }

  else if(node->right){
    insertBT(node->right, name, address, number);
  }

  else{
    node->left = createNode(name, address, number);
  }
}

struct node* inorderpre(struct node* node){

  while(node->right != NULL){
      node = node->right;
  }

   return node;

}

// Our function to remove a given node from the tree.
struct node* removeBT(struct node *root, char *name){

  if(root == NULL){
     return root;
  }

  if(strcmp(root->name, name) > 0){
      root->left = removeBT(root->left, name);
  }

  else if(strcmp(root->name, name) < 0){
      root->right = removeBT(root->right, name);
  }

  else {
      if(root->left == NULL){
          struct node* temp = root->right;
          free(root);
          return temp;
      }

      else if(root->right == NULL){
          struct node* temp = root->left;
          free(root);
          return temp;
      }

      struct node* temp = inorderpre(root->left);
      strcpy(root->name, temp->name);
      root->left = removeBT(root->left, temp->name);
  }

  return root;
}

// Our function to search the binary tree by name.
void searchBTname(struct node *root, char *name){

    char name1[50];
    char name2[50];

    strcpy(name1, root->name);
    strcpy(name2, name);

    if(!strcmp(toLowercase(name1), toLowercase(name2))){
        printNode(root);
    }

    if(root->left){
        searchBTname(root->left, name);
    }

    if(root->right){
        searchBTname(root->right, name);
    }
}

// Our function to search the binary tree by number.
void searchBTnumber(struct node *root, int number){
    if(root->number == number){
        printNode(root);
    }

    if(root->left){
        searchBTnumber(root->left, number);
    }

    if(root->right){
        searchBTnumber(root->right, number);
    }
}

// Printing a node of the tree in style.
void printNode(struct node *node){
    printf("-----------------------\n");
    printf("Name: %s \nAddress: %s \nNumber: %d\n", node->name, node->address, node->number);
    printf("-----------------------\n");
}

// A function which converts a given string into lowercase.
// Since a string is an array of characters in C, we simply use the tolower function on each character.	
const char* toLowercase(char *str){

    int j = 0;
    while (str[j]) {
        str[j] = tolower(str[j]);
        j++;
    }

    return str;
}
