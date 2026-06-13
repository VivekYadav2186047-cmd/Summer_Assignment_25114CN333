# Write a program to Input and display array.


n = int(input("enter the number of elements = "))
array = []

for i in range(n):
    number = int(input("enter element = "))
    array.append(number)

print("Array elements are:")
for i in array:
    print(i, end=" ")
