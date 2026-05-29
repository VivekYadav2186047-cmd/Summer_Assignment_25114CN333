#include <stdio.h>
int main(){
    /*Write a program to Check whether a number is 
palindrome.*/
int n , d , rev = 0, temp;
printf("enter the number n = ");
scanf("%d", &n);
temp = n;
while(n>0){
    d = n%10;
    rev = rev*10 + d;
    n = n/10;
}
if(rev == temp)
printf("number is palindrome");
else
printf("not palindrome");
return 0;
}
