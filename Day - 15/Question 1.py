#Write a program to Reverse array. 

n = int(input("enter the number of elements = "))

# Input array elements
array = []
for i in range(n):
    element = int(input(f"enter element {i+1} = "))
    array.append(element)

# Reverse the array
array.reverse()

# Display reversed array
print("Reversed array:", array)
