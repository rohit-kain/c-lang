#include<stdio.h>
int main(){
    int n;
    printf("enter a number\t");
    scanf("%d",&n);
  
    if(n%2==0){
        printf("%d is a even numbr\n",n);

    }
    else{
        printf("%d is odd number\n",n);
    }
    return 0;

}