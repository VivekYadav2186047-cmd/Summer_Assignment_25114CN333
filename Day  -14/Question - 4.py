#Write a program to Find duplicates in array. 
n = int(input("enter the number of elements = "))
array = []
for i in range(n):
    array.append(int(input("enter element = ")))

duplicates = []
for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if array[i] == array[j] and array[i] not in duplicates:
            duplicates.append(array[i])

print("Duplicate elements are:", duplicates)
