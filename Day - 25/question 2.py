# Write a program to Find common characters 
# in strings. 
str1 = input("enter first string = ")
str2 = input("enter second string = ")

print("Common characters:", end=" ")
for ch in str1:
    if ch in str2:
        print(ch, end=" ")
