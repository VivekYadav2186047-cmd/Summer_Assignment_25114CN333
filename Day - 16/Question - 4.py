# Write a program to Remove duplicates from 
# array. 
n = int(input("enter number of elements = "))
array = []
for i in range(n):
    array.append(int(input()))

unique = []
for number in array:
    if number not in unique:
        unique.append(number)

print("Array after removing duplicates:")
print(unique)
