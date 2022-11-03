// Tree traversal in C

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct node {
  char name[50];
  char address[50];
  int number;

  struct node* left;
  struct node* right;
};

// Inorder traversal
void inorderTraversal(struct node* root) {
  if (root == NULL){
      return;
  }

  inorderTraversal(root->left);
  printf("%d ->", root->number);
  inorderTraversal(root->right);
}

struct node* createNode(char* name, char* address, int number) {
  struct node* newNode = malloc(sizeof(struct node));
  strcpy(newNode->name, name);
  strcpy(newNode->address, address);
  newNode->number = number;

  newNode->left = NULL;
  newNode->right = NULL;

  return newNode;
}

// Insert on the left of the node
struct node* insertLeft(struct node *root, char* name, char* address, int number) {
  root->left = createNode(name, address, number);

  return root->left;
}

struct node* insertRight(struct node *root, char* name, char* address, int number) {
  root->right = createNode(name, address, number);

  return root->right;
}

void printTree(struct node *p)
{
    /*If tree has nodes:*/
    if (p != NULL) {
        /*Print node data.*/
        printTree(p->left);
        printf("%s %s %d\n", p->name, p->address, p->number);
        printTree(p->right);
    }
}
