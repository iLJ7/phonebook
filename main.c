/* See README for instructions on how to use the phonebook */

#include <stdio.h>
#include "utility.c" /* Including our utility function */
#include <string.h>

int main()
{
   greet(); // We greet the user.

   struct node* root = createNode("ROOT", "ROOT-ADDRESS", 1);     // We create a non-entry root to serve as a base for inserting into our tree.

   char str[100];
   int i;

   while(1){                            // We create a while loop to repeatedly ask for commands, until the user enters quit.
       printf("Enter a command: \n");
       scanf("%s", str);

       if(!strcmp(str, "print")){
           printTree(root);
       }

       if(!strcmp(str, "search")){
           search(root);
       }                                        // We call the respective functions from the utility file.

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
