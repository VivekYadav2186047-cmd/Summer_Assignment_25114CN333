#Write a program to Find maximum frequency 
#element.
n = int(input("enter number of elements = "))

array = []
for i in range(n):
    array.append(int(input()))
max_element = array[0]
max_freq = array.count(array[0])
for element in array:
    freq = array.count(element)
    if freq > max_freq:
        max_freq = freq
        max_element = element

print(" maximum frequency element:", max_element)
print("frequency:", max_freq) 
