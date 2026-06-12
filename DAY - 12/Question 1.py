def palindrome(number):
    original = number
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10

    return original == reverse

# Taking input from the user
number = int(input("enter a number = "))
if palindrome(number):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
