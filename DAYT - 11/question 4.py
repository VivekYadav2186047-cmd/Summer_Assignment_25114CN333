# Write a program to Write function to find 
# # factorial. 
def factorial(num):
    fact = 1
    for i in range(1, 1 + num):
        fact = fact*i
    return fact
#taking input from the user
num = int(input("enter the number = "))
#calling the function
print("factorial of a given numbber =" , factorial(num))
              
