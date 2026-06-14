# Write a program to Linear search. 

array = [10, 20, 30, 40, 50]
key = int(input("enter element to search = "))
found = False

for i in range(len(array)):
    if array[i] == key:
        print("element found at index", i)
        found = True
        break

if not found:
    print("element not found")
