# que = Write a program to Convert binary to decimal
binary = input("Enter a binary number = ")
#taking input from the user

decimal = 0 #store final decimal value
power = 0

for digit in binary[::-1]:
    decimal = decimal + int(digit) * (2 ** power)
    power += 1

print("Decimal num = ", decimal)
