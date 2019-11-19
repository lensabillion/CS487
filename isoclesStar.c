#include <stdio.h>
int main(){
     int input;

    /* Input number of rows to print */
    printf("Enter your number of rows : ");
    scanf("%d", &input);
    for(int i=0; i<=input; i++)
    {
        for(int j=i; j<input; j++)
        {
            printf(" ");
        }


        for(int k=1; k<=(2*i-1); k++)
        {
            printf("*");
        }


        printf("\n");


    }
return 0;
}

