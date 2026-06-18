#Write a program to Sort array in descending order


n = int(input("enter number of elements = "))

arr = []
for i in range(n):
    arr.append(int(input("enter element = ")))

# sort in descending order
arr.sort(reverse=True)

print("Array in descending order:")
print(arr)
