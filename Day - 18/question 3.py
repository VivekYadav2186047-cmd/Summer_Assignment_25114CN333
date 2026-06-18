#Write a program to Binary search.


n = int(input("enter number of elements = "))

array = []
for i in range(n):
    array.append(int(input("enter element = ")))

key = int(input("enter element to search = "))

low = 0
high = n - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if array[mid] == key:
        print("element found at index", mid)
        found = True
        break
    elif array[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element not found")
