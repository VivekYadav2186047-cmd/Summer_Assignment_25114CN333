#Write a program to Merge arrays. 
array1 = input("enter first array = ").split()

array2 = input("enter second array = ").split()


for item in array2:
    array1.append(item)

print("Merged Array:", array1)
