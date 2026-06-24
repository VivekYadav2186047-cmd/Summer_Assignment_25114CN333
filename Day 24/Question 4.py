#Write a program to Remove duplicate characters.

string = input("Enter a string: ")

result = ""

for char in string:
    if char not in result:
        result += char

print("String after removing duplicates:", result) 
