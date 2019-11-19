#include <stdio.h>
int main(){
    int input;
    printf("Enter your a number of rows:");
    scanf("%d",&input);

    for(int i=0;i<input;i++){
        for(int j=0;j<=i;j++){
            printf("*");
        }
        printf("\n");
    }
return 0;
}
