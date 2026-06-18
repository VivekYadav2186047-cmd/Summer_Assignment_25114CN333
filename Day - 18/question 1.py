#Write a program to Bubble sort. 


n = int(input("enter number of elements = "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

# Bubble Sort
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print("Sorted array:")
print(arr)
