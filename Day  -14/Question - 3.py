#Write a program to Second largest lement. 


array = [10, 20, 5, 40, 30]
largest = second_largest = float('-inf')
for number in array:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest and number != largest:
        second_largest = number

print("Second largest element is:", second_largest)
