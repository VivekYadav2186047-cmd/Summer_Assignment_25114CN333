#include <stdio.h>
int main(){
    /*Write a program to Reverse a number. */
    int n , d;
    printf("enter the number n=");
    scanf("%d", &n);
    int rev =0;
    while(n>0){
        d = n%10;
        rev = rev*10 + d;
        n = n/10;
    }
    printf("reverse of a number is %d", rev);
    return 0;
}