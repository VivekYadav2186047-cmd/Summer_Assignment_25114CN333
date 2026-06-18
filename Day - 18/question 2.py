#Write a program to Selection sort.


n = int(input("enter number of elements = "))

array = []
for i in range(n):
    array.append(int(input("enter element = ")))

# Selection Sort
for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if array[j] < array[min_index]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i]

print("Sorted array:")
print(array)
