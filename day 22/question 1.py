#Write a program to Check palindrome string.
string = input("Enter the string :")


if(string == string[::-1]):
    print("string is palindrome")

else:
    print("not palindrome")
