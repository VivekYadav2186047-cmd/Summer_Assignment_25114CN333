
# Program to count even and odd elements in an array

n = int(input("enter the number of elements = "))

array = []
for i in range(n):
    number = int(input("Enter element: "))
    array.append(number)

even_count = 0
odd_count = 0
for number in array:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("number of even elements =", even_count)
print("number of odd elements =", odd_count)
