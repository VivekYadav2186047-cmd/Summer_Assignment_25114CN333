#include <stdio.h>
int main(){
    /*Write a program to Find sum of digits of a 
number. */
int n , d , s = 0;
printf("enter the number n =");
scanf("%d", &n);
while(n>0){
    d = n%10;
    s = s + d;
    n = n/10;
}
printf("the sum of digit is %d", s);
return 0;
}
