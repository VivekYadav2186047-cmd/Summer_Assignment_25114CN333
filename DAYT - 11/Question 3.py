# Write a program to Write function to check prime.

def prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

# Taking input from the user
number = int(input("enter a number = "))

# Calling  function
if prime(number):
    print(number, "is a Prime Number")
else:
    print(number, "is not a Prime Number")
