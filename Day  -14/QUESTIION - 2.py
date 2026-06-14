# Write a program to Frequency of an element. 

arrar = [10, 20, 30, 20, 40, 20, 50]

key = int(input("enter element to find frequency =  "))

count = 0
for i in arrar:
    if i == key:
        count += 1

print("Frequency of", key, "is", count)
