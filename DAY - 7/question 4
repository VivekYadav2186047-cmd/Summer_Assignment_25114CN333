# Write a program to Recursive reverse number.

def reverse_num(n, reverse=0):
    if n == 0:  # base condition
        return reverse
    reverse = reverse * 10 + (n % 10)
    return reverse_num(n // 10, reverse)

num = int(input("Enter a number: "))
print("Reversed number =", reverse_num(num))
