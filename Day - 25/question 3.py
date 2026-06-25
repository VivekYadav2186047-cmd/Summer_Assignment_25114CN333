# Write a program to Sort names 
# alphabetically. 
n = int(input("enter the number of names: "))

names = []
for i in range(n):
    name = input(f"enter name {i + 1}: ")
    names.append(name)

names.sort()
print("names in alphabetical order:")
for name in names:
    print(name)
