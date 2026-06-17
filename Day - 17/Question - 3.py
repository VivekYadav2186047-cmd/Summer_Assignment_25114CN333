#Write a program to Intersection of arrays. 
array1 = [int(x) for x in input("enter first array = ").split()]

array2 = [int(x) for x in input("enter second array = ").split()]



intersection = list(set(array1) & set(array2))

print("Intersection of arrays:", intersection)
