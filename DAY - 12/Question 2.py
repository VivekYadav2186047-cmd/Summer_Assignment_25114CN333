# Write a program to Write function for 
# Armstrong. 
def armstrong(number):
    digits = len(str(number))
    temp = number
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit**digits
        temp //= 10

    return total==number

# Taking input from the user
number = int(input("enter a number = "))
if armstrong(number):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
