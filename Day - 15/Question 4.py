#Write a program to Move zeroes to end. 
n = int(input("enter the number of elements = "))
array = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    array.append(element)

# Separate non-zero and zero elements
non_zero = []
zero_count = 0
for num in array:
    if num != 0:
        non_zero.append(num)
    else:
        zero_count += 1

# Add zeroes at the end
result = non_zero + [0] * zero_count

print("Array after moving zeroes to the end:", result)
