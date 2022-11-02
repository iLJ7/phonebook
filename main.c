/* hello.c
   A first program in C */

#include <stdio.h>
#include "utility.h"
#include "binaryTree.h"
#include <string.h>

int main()
{
   struct node* root = createNode(1);
   insertLeft(root, 2);
   insertRight(root, 3);

   insertLeft(root->left, 4);

   char str[100];
   int i;

   printf( "Enter a command :\n");
   scanf("%s", str);

   if(!strcmp(str, "print")){
       printTree(root);
   }
   return 0;
}
