
# Program to find sum and average of an array

n = int(input("enter the number of elements = "))
array = []
for i in range(n):
    number = int(input("Enter element: "))
    array.append(number)

total = sum(array)
average = total / n

print("Sum =", total)
print("Average =", average)
