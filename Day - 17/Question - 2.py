#Write a program to Union of arrays. 
array1 = [int(x) for x in input("enter first array = ").split()]

array2 = [int(x) for x in input("enter second array = ").split()]


union = list(set(array1 + array2))
print("Union of arrays:", union)
