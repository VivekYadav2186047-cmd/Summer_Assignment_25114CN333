#include <stdio.h>
int main(){
    /*Write a program to Find product of digits. */
    int n , d , pro = 1;
    printf("enter the nuber n=");
    scanf("%d", &n);
    while(n>0){
        d = n%10;
        pro= pro*d;
        n = n/10;
    }
    printf("product of a given number is %d", pro);
    return 0;
}