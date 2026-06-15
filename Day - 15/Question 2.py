#Write a program to Rotate array left. 
n = int(input("enter the number of elements = "))
array = []
for i in range(n):
    element = int(input(f"enter element {i+1} = "))
    array.append(element)

# Number of positions to rotate
k = int(input("Enter the number of positions to rotate left: "))

# Handle rotations greater than array size
k = k % n

# Left rotation
rotated_array = array[k:] + array[:k]

print("Array after left rotation:", rotated_array)
