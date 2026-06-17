#Write a program to Find common elements

array1 = [int(x) for x in input("enter first array = ").split()]

array2 = [int(x) for x in input("enter second array = ").split()]

common = []

for num in array1:
    if num in array2 and num not in common:
        common.append(num)

print("Common elements:", common)
