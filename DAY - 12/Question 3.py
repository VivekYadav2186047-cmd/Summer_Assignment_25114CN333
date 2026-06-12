#Write a program to Write function for 
#Fibonacci.
def fibonacci(number):
    a, b = 0, 1
    for i in range(number):
        print(a, end=" ")
        a, b = b, a + b

# Taking input from the user
terms = int(input("enter the number of terms = "))

fibonacci(terms) 
