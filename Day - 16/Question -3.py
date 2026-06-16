# Write a program to Find pair with given sum.
n = int(input("enter number of elements = "))

array = []
for i in range(n):
    array.append(int(input()))
target = int(input("enter the target sum = "))

found = False
for i in range(n):
    for j in range(i + 1, n):
        if array[i] + array[j] == target:
            print("Pair found:", array[i], array[j])
            found = True
if not found:
    print("No pair found")
