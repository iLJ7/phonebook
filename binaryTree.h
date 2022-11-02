
// Tree traversal in C

#include <stdio.h>
#include <stdlib.h>

struct phoneTree {
  char name[];
  char address[];
  char phone[];
}

struct node {
  int item;
  struct node* left;
  struct node* right;
};

// Inorder traversal
void inorderTraversal(struct node* root) {
  if (root == NULL){
      return;
  }

  inorderTraversal(root->left);
  printf("%d ->", root->item);
  inorderTraversal(root->right);
}

struct node* createNode(int value) {
  struct node* newNode = malloc(sizeof(struct node));
  newNode->item = value;
  newNode->left = NULL;
  newNode->right = NULL;

  return newNode;
}

// Insert on the left of the node
struct node* insertLeft(struct node* root, int value) {
  root->left = createNode(value);

  return root->left;
}

struct node* insertRight(struct node* root, int value) {
  root->right = createNode(value);

  return root->right;
}

void printTree(struct node *p)
{
    /*If tree has nodes:*/
    if (p != NULL) {
        /*Print node data.*/
        printTree(p->left);
        printf("%d\n", p->item);
        printTree(p->right);
    }
}