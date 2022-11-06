/* hello.c
   A first program in C */

#include <stdio.h>
#include "utility.c"
#include <string.h>

int main()
{
   struct node* root = createNode("Luke", "Robinstown", 50);
   insertLeft(root, "Cian", "Rathbridge", 100);
   insertRight(root, "Alex", "Vegetable", 150);

   char str[100];
   int i;

   while(1){
       printf("Enter a command: \n");
       scanf("%s", str);

       if(!strcmp(str, "print")){
           printTree(root);
       }

       if(!strcmp(str, "store")){
           insert(root);
       }

       if(!strcmp(str, "remove")){
           removeUtil(root);
       }

       if(!strcmp(str, "quit")){
           break;
       }
   }

   return 0;
}
