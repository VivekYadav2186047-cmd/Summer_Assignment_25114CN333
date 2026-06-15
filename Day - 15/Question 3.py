#Write a program to Rotate array right.
n = int(input("enter the number of elements = "))
array = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    array.append(element)

# Number of positions to rotate
k = int(input("Enter the number of positions to rotate right: "))

# Handle rotations greater than array size
k = k % n

# Right rotation
rotated_arr = array[-k:] + array[:-k]
print("Array after right rotation:", rotated_arr)
