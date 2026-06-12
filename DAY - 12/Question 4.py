# Write a program to Write function for perfect 
# number. 
def perfect_number(number):
    total = 0
    for i in range(1, number):
        if number % i == 0:
            total += i

    return total==number

# Taking input from the user
number = int(input("enter a number = "))

if perfect_number(number):
    print("Perfect Number")
else:
    print("Not a Perfect Number")
