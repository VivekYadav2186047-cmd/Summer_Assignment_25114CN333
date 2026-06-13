
# Program to find the largest and smallest element in an array

n = int(input("enter the number of elements = "))
array = []
for i in range(n):
    number = int(input("enter element = "))
    array.append(number)

largest = array[0]
smallest = array[0]
for i in array:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("largest element =", largest)
print("smallest element =", smallest)
