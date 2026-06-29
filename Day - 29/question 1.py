# Write a program to Create menu-driven 
# calculator. 
try:
    a = int(input("Enter the number a :"))
    b = int(input("Enter the nnmber b : "))
    print("What kind of operation do you want to perform?\n press + for addition \n press - for subtraction \n press * for subtraction \n press / for division")

    o = input("Enter the operation :")
    match o:
        case "+":
            print(f"the result is {a + b}")
        case "-":
            print(f"the result is {a - b}")
        case "*":
            print(f"the result is {a * b}")
        case "/":
            print(f"the result is {a / b}")

except Exception as e:
    print("Enter a valid value of a and b")
